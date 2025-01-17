import socket as mysoc
import sys

def client(rsHostname, rsListenPort, tsListenPort):
# Establishing socket for root server
    try:
        rs = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Root server-client socket created")
    except mysoc.error as err:
        print("[C]: Root server-client socket open error")

# Connect to the root server

    if rsHostname.lower() == "localhost":
        rs_addr = mysoc.gethostbyname(mysoc.gethostname())
    else:
        rs_addr = mysoc.gethostbyname(rsHostname.lower())
    rs_server_binding=(rs_addr, int(rsListenPort))
    rs.connect(rs_server_binding)
    
# Open output files
    output_file = open("RESOLVED.txt", "w")

# Variable to store ts socket
    ts = None

# Iterate input file line by line
    with open("PROJI-HNS.txt") as input_file:
        for line in input_file:

            hostname = line.lower().rstrip()

            # Send request for hostname
            rs.send(hostname.encode('utf-8'))
            print("[C] Sent: " + hostname)
            response = rs.recv(1024).decode('utf-8')
            print("[C] Response: " + response)

            # Check response
            response_split = response.lower().split()
            # Root server found a match, output
            if(response_split[2] == "a"):
                output_file.write(response + '\n')
            # Root server returned another name server
            elif(response_split[2] == "ns"):
                # Create second socket for ts
                if(ts == None):
                    try:
                        ts = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
                        print("[C]: Top-level client socket created")
                    except mysoc.error as err:
                        print("[C]: Top-level socket open error")

                    # Connect to top-level server
                    if response_split[0].lower() == "localhost":
                        ts_addr = mysoc.gethostbyname(mysoc.gethostname())
                    else:
                        ts_addr = mysoc.gethostbyname(response_split[0].lower())
                    ts_server_binding = (ts_addr, int(tsListenPort))
                    ts.connect(ts_server_binding)

                # Send hostname
                ts.send(hostname.encode('utf-8'))
                print("[C] Sent: " + hostname)
                # Response is added to output no matter what
                response = ts.recv(1024).decode('utf-8')
                print("[C] Response: " + response)
                output_file.write(response + '\n')
            else:
                print("[C] Malformed response.")
                exit()
    
    print("[C]: Done, terminating connections.")

# Close output file
    output_file.close()

# Close the root server socket
# Close connections and sockets
    if(ts != None):
        ts.close()
    rs.close()
    exit()

client(sys.argv[1], sys.argv[2], sys.argv[3])
