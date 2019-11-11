#!/usr/bin/env python3

import argparse
import logging
import select
import socket
import socketserver
from typing import Tuple

__doc__ = 'Proxy server example: simple responses for requests'

logger = logging.getLogger('simple-proxy')


class ProxyConnectionHandler(socketserver.BaseRequestHandler):
    remote_address: Tuple[str, int]
    __BUFFER_SIZE = 2048

    def handle(self):
        logger.info('Incoming connection from {}:{}'.format(*self.client_address))

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as outbound_socket:
            logger.info('Connecting to {}:{}'.format(*self.__class__.remote_address))
            outbound_socket.connect(self.__class__.remote_address)

            # Here we can do modification with the data

            logger.info('Switch to transparent-proxy mode')
            while True:
                input_ready_sockets, _, _ = select.select([outbound_socket, self.request], [], [])
                for source_socket in input_ready_sockets:
                    destination_socket = self.request if source_socket is outbound_socket else outbound_socket
                    try:
                        self.__forward(source_socket, destination_socket)
                    except ConnectionResetError:
                        return

    def __forward(self, source_socket, destination_socket):
        data = self.__receive(source_socket)
        self.__send(destination_socket, data)

    def __receive(self, receiver_socket: socket.socket):
        data = receiver_socket.recv(self.__class__.__BUFFER_SIZE)
        if data == b'':
            raise ConnectionResetError

        if logger.isEnabledFor(logging.DEBUG):
            source = 'C' if receiver_socket is self.request else 'S'
            logger.debug('[{}=>P] {!r}'.format(source, data))

        return data

    def __send(self, sender_socket: socket.socket, data):
        if logger.isEnabledFor(logging.DEBUG):
            destination = 'C' if sender_socket is self.request else 'S'
            logger.debug('[P=>{}] {!r}'.format(destination, data))

        sender_socket.sendall(data)


def __address_type(address: str) -> Tuple[str, int]:
    try:
        host, port = address.split(':', 1)
        return host, int(port)
    except Exception as e:
        raise argparse.ArgumentTypeError(repr(e))


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'remote_address',
        type=__address_type,
        nargs='?',
        action='store',
        default='localhost:1422',
        help='Remote host:port (default: %(default)s)',
    )
    parser.add_argument(
        'bind_address',
        type=__address_type,
        action='store',
        nargs='?',
        default='localhost:1421',
        help='Local bind host:port (default: %(default)s)',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        dest='verbosity',
        default=0,
        help='Increase verbosity (max: -vv)'
    )

    args = parser.parse_args()
    args.log_level = (logging.WARNING, logging.INFO, logging.DEBUG)[min(args.verbosity, 2)]

    return args


def main():
    args = parse_arguments()
    logging.basicConfig(
        level=args.log_level,
        format='%(asctime)s %(levelname)-7s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    ProxyConnectionHandler.remote_address = args.remote_address

    server = socketserver.TCPServer(args.bind_address, ProxyConnectionHandler, bind_and_activate=False)
    server.allow_reuse_address = True
    server.server_bind()
    server.server_activate()

    with server as server:
        logger.info('Ready on {}:{}'.format(*args.bind_address))
        server.serve_forever()


if __name__ == '__main__':
    main()
