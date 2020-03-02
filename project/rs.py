import socket as mysoc
import sys

def root_server(rsListenPort):

# We must track the top-level hostname for the purposes of this project
    tsHostname = ""

# Track hostname ip pairs as a dictionary
    table = {}

    # Load file into dictionary
    with open("PROJI-DNSRS.txt") as input_file:
        for line in input_file:
            entry = line.lower().split()

            # We must check each entry's type, in order to be able to define our tsHostname
            # Ignore invalid entries
            if(len(entry) != 3):
                continue
            # This entry specifies the top-level name server, track it
            if(entry[2] == "ns"):
                tsHostname = entry[0]
            # Normal entry
            elif(entry[2] == "a"):
                hostname = entry[0]
                table[hostname] = entry[1] + " " + entry[2]

# Establish sockets for hosting
    try:
        rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[RS]: Root server socket created")
    except mysoc.error as err:
        print("[RS]: Root socket open error")

# Open server and begin listening
    server_binding=('', int(rsListenPort))
    rs.bind(server_binding)
    rs.listen(1)

# Begin accepting requests
    host = mysoc.gethostname()
    print("[S]: Server host name is: ", host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is: ", localhost_ip)

# Accept a request from clients
    csockid,addr = rs.accept()
    print("[S]: Got a connection request from a client at", addr)

# Receive and process a hostname request
    hostname = csockid.recv(1024).decode('utf-8')
    print("[S]: Hostname requested from client: " + hostname)

# 
    if hostname in table:
        response = hostname + " " + table[hostname]
    else:
        response = tsHostname + " - ns"

    csockid.send(response.encode('utf-8'))
    print("[S]: Sent response: " + response)
    
   # Close the server socket
    rs.close()
    exit()

root_server(sys.argv[1])
