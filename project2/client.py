import socket as mysoc
import sys

def client(lsHostname, lsListenPort):
# Establishing socket for root server
    try:
        ls = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Load server-client socket created")
    except mysoc.error as err:
        print("[C]: Load server-client socket open error")

# Connect to the root server

    if lsHostname.lower() == "localhost":
        ls_addr = mysoc.gethostbyname(mysoc.gethostname())
    else:
        ls_addr = mysoc.gethostbyname(lsHostname.lower())
    ls_server_binding=(ls_addr, int(lsListenPort))
    ls.connect(ls_server_binding)
    
# Open output files
    output_file = open("RESOLVED.txt", "w")

# Iterate input file line by line
    with open("PROJ2-HNS.txt") as input_file:
        for line in input_file:

            hostname = line.lower().rstrip()

            # Send request for hostname
            ls.send(hostname.encode('utf-8'))
            print("[C] Sent: " + hostname)
            response = ls.recv(1024).decode('utf-8')
            print("[C] Response: " + response)
            output_file.write(response + '\n')
    
    print("[C]: Done, terminating connections.")

# Close output file
    output_file.close()

# Close connections and sockets
    ls.close()
    exit()

client(sys.argv[1], sys.argv[2])
