import socket as mysoc
import sys

def top_server(tsListenPort):

# Track hostname ip pairs as a dictionary
    table = {}

    # Load file into dictionary
    with open("PROJI-DNSTS.txt") as input_file:
        for line in input_file:
            entry = line.lower().split()

            # We must check each entry's type, in order to be able to define our tsHostname
            # Ignore invalid entries
            if(entry[2] == "a"):
                hostname = entry[0]
                table[hostname] = entry[1] + " " + entry[2]
            else:
                continue

# Establish sockets for hosting
    try:
        ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[TS]: Top-level server socket created")
    except mysoc.error as err:
        print("[TS]: Top-level socket open error")

# Open server and begin listening
    server_binding=('', int(tsListenPort))
    ts.bind(server_binding)
    ts.listen(1)

# Begin accepting requests
    host = mysoc.gethostname()
    print("[TS]: Server host name is: ", host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[TS]: Server IP address is: ", localhost_ip)

# Accept a request from clients
    csockid,addr = ts.accept()
    print("[TS]: Got a connection request from a client at", addr)

# Receive and process a hostname request
    hostname = csockid.recv(1024).decode('utf-8')
    print("[TS]: Hostname requested from client: " + hostname)

# Check if hostname is in table, otherwise return error message
    if hostname in table:
        response = hostname + " " + table[hostname]
    else:
        response = hostname + " - Error:HOST NOT FOUND"

    csockid.send(response.encode('utf-8'))
    print("[TS]: Sent response: " + response)
    
   # Close the server socket
    ts.close()
    exit()

top_server(sys.argv[1])
