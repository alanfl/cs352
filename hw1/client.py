import socket as mysoc

def client():
# Establishing socket
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

# Define the port on which you want to connect to the server
    port = 50009
# Connect to the server on local machine
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

# First, confirm that the connection was successful and that the server is ready
    msg = cs.recv(100).decode('utf-8')

    if(msg != "Welcome to CS 352"):
        print("Error: server response was invalid.")
        exit()
    
# Send number of lines to server
    with open("HW1test.txt") as input_file:
        num_lines = 0
        for line in input_file:
            num_lines = num_lines + 1
        input_file.close()

    cs.send(str(num_lines).encode('utf-8'))
    msg = cs.recv(100).decode('utf-8')

    if(msg != "OK"):
        print("Error: server line response was invalid.")
        exit()

    cs.send(("Sending").encode('utf-8'))
    print("[C]: Sending...")
    
# Next, attempt to open files
    output_file = open("HW1out.txt", "w")

# Iterate file line by line
    with open("HW1test.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            cs.send(line.encode('utf-8'))
            print("[C] Sent: " + line)
            response = cs.recv(100).decode('utf-8')
            print("[C] Response: " + response)
            output_file.write(line)
        
# close the cclient socket
    cs.close()
    exit()

client()
