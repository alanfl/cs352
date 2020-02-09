import socket as mysoc

def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50009)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print("[S]: Got a connection request from a client at", addr)

# send a intro  message to the client.
    msg="Welcome to CS 352"
    csockid.send(msg.encode('utf-8'))

# await number of lines from client
    num_lines = csockid.recv(100).decode('utf-8')
    print("[S]: Receiving lines: " + num_lines)
    if(isinstance(int(num_lines), int) == False):
        print("[S]: Invalid message from client.")
        exit()
    
    csockid.send("OK".encode('utf-8'))

# await confirmation for sending
    confirm = csockid.recv(100).decode('utf-8')
    if(confirm != "Sending"):
        print("[S]: Invalid message from client.")
        exit()

    print("Receiving...")

    for x in range(0, int(num_lines)):
        output = csockid.recv(100).decode('utf-8')
        print("[S]: Message from client: " + output)
        response = translate(output)
        csockid.send(response.encode('utf-8'))
        print("[S]: Sent response: " + response)
    
   # Close the server socket
    ss.close()
    exit()

# translate str to ASCII as 1_2_3 for example
def translate(msg):
    trans = ""
    for char in msg:
        trans += str(ord(char)) + "_"
    return trans.rstrip("_")

server()
