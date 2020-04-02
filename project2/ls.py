import socket as mysoc
import select
import sys

def load_server(lsListenPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort):

# Establish sockets for hosting
    try:
        ls = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[LS]: Load server socket created")
    except mysoc.error as err:
        print("[LS]: Load socket open error")

# Establish socket for ts1 server
    try:
        ts1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[LS]: ts1 server socket created")
    except mysoc.error as err:
        print("[LS]: ts1 socket open error")

# Connect to ts1
    if ts1Hostname.lower() == "localhost":
        ts1_addr = mysoc.gethostbyname(mysoc.gethostname())
    else:
        ts1_addr = mysoc.gethostbyname(ts1Hostname.lower())
    ts1_server_binding = (ts1_addr, int(ts1ListenPort))
    ts1.connect(ts1_server_binding)

# Establish socket for ts2 server
    try:
        ts2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[LS]: ts2 server socket created")
    except mysoc.error as err:
        print("[LS]: ts2 socket open error")

# Connect to ts2
    if ts1Hostname.lower() == "localhost":
        ts2_addr = mysoc.gethostbyname(mysoc.gethostname())
    else:
        ts2_addr = mysoc.gethostbyname(ts2Hostname.lower())
    ts2_server_binding = (ts2_addr, int(ts2ListenPort))
    ts2.connect(ts2_server_binding)


# Open server and begin listening
    server_binding=('', int(lsListenPort))
    ls.bind(server_binding)
    ls.listen(1)

# Begin accepting requests
    host = mysoc.gethostname()
    print("[LS]: Server host name is: ", host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[LS]: Server IP address is: ", localhost_ip)

# Accept a request from clients
    csockid,addr = ls.accept()
    print("[LS]: Got a connection request from a client at", addr)

    while True:
            hostname = csockid.recv(1024).decode('utf-8')
            print("[LS]: Hostname requested from client: " + hostname)

            if(hostname != ""):
                # Forward requests to ts servers
                ts1.send(hostname.encode('utf-8'))
                ts2.send(hostname.encode('utf-8'))

                target_server = select.select([ts1, ts2], None, None, 5000)
                if(target_server):
                    response = target_server.recv(1024).decode('utf-8')
                else:
                    response = hostname + " - Error:HOST NOT FOUND"
            else:
                print("[LS]: Terminating connection.")
                break
            
            # Send the response
            csockid.send(response.encode('utf-8'))
            print("[LS]: Sent response: " + response)
    
   # Close the server socket
    ls.close()
    exit()

load_server(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
