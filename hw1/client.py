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

    if(msg == )

# Receive data from the server
    data_from_server=cs.recv(100)

    print("[C]: Data received from server::  ",data_from_server.decode('utf-8'))
# close the cclient socket
    cs.close()
    exit()