import socket as mysoc
import sys

def top_server(tsListenPort):

# Track hostname ip pairs as a dictionary
    table = {}

    # Load file into dictionary
    with open("PROJ2-DNSTS1.txt") as input_file:
        for line in input_file:
            entry = line.split()

            # We must check each entry's type, in order to be able to define our tsHostname
            # Ignore invalid entries
            if(entry[2].lower() == "a"):
                hostname = entry[0].lower()
                table[hostname] = entry[1] + " " + entry[2]
            else:
                continue

# Establish sockets for hosting
    try:
        ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[TS1]: Top-level server socket created")
    except mysoc.error as err:
        print("[TS1]: Top-level socket open error")

# Open server and begin listening
    server_binding=('', int(tsListenPort))
    ts.bind(server_binding)
    ts.listen(1)

# Begin accepting requests
    host = mysoc.gethostname()
    print("[TS1]: Server host name is: ", host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[TS1]: Server IP address is: ", localhost_ip)

# Accept a request from clients
    csockid,addr = ts.accept()
    print("[TS1]: Got a connection request from a client at", addr)

# Receive and process hostname requests
    while True:
        hostname = csockid.recv(1024).decode('utf-8')
        print("[TS1]: Hostname requested from client: " + hostname)

        response = ""

        if(hostname != ""):
            # Check if hostname is in table, otherwise return error message
            if hostname.lower() in table:
                response = hostname + " " + table[hostname]
                csockid.send(response.encode('utf-8'))
        else:
            print("[TS1]: Terminating connection.")
            break

        print("[TS1]: Sent response: " + response)
    
   # Close the server socket
    ts.close()
    exit()

top_server(sys.argv[1])
