You can try this script out as follows:

We need three terminal windows:

First terminal: run the script: "./simple_proxy.py"
    Now, the remote address will be localhost:1422 and the inbound address shall be localhost:1421

Second terminal: run "nc -l localhost 1422" to listen whether th data is sent to the remote address

Third terminal: run "echo HELLO | nc localhost 1421"

We should make sure that the word HELLO is arrived at address localhost:1422
