import socket as mysoc

def client():
# Establishing socket
    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

# Define the port on which you want to connect to the server
    port = 50007
# Connect to the server on local machine
    sa_sameas_myaddr =mysoc.gethostbyname(mysoc.gethostname())
    server_binding=(sa_sameas_myaddr,port)
    cs.connect(server_binding)

# First, confirm that the connection was successful and that the server is ready
    msg = cs.recv(100)

    if(msg != "Welcome to CS 352"):
        print("Error: server response was invalid.")
    

# Next, attempt to open files
    input_filepath = "HW1test.txt"
    output_filepath = "HW1out.txt"
    input_file = open(input_filepath, "r")
    output_file = open(output_filepath, "w")
    
# Iterate file line by line
    for line in input_file:
        cs.send(line)
        print("Sent: " + line)
        response = cs.recv(100).decode('utf-8')
        print("Response: " + response)
        output_file.write(line)
        
# close the cclient socket
    cs.close()
    exit()

client()