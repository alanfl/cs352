import socket as mysoc

def client(rsHostname, rsListenPort, tsListenPort):
# Establishing socket
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print("[{} \n".format(]"socket open error ",err))

# Define the ports for the root-level DNS server
    rs_port = 50009
# Connect to the root-level server on local machine
    myaddress = mysoc.gethostbyname(mysoc.gethostname())
    server_binding=(myaddress, rs_port)
    rs.connect(server_binding)

# First, confirm that the connection was successful and that the server is ready
    msg = cs.recv(1024).decode('utf-8')

    if(msg != "Welcome to CS 352"):
        print("Error: server response was invalid.")
        exit()
    
# Next, attempt to open files
    output_file = open("HW1out.txt", "w")

# Iterate file line by line
    with open("HW1test.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            cs.send(line.encode('utf-8'))
            print("[C] Sent: " + line)
            response = cs.recv(1024).decode('utf-8')
            print("[C] Response: " + response)
            output_file.write(response + '\n')
    
    print("[C]: Done, terminating connection.")
    cs.send("".encode('utf-8'))
# close the cclient socket
    cs.close()
    exit()

client()
