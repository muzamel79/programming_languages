#!/usr/bin/env python3

import sys


def main(*raw_args: str):
    print('Hello World!')

    for arg in raw_args:
        print(arg)


if __name__ == '__main__':
    main(*sys.argv[1:])
