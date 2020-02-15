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

    while True:
        msg = csockid.recv(1024).decode('utf-8')
        print("[S]: Message from client: " + msg)
        if(msg != ""):
            response = translate(msg)
            csockid.send(response.encode('utf-8'))
            print("[S]: Sent response: " + response)
        else:
            print("[S]: Terminating connection.")
            break
    
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
