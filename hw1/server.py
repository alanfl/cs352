import socket as mysoc

def server():
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    server_binding=('',50007)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)
    csockid,addr=ss.accept()
    print ("[S]: Got a connection request from a client at", addr)
# send a intro  message to the client.
    msg="Welcome to CS 352"
    csockid.send(msg.encode('utf-8'))

    while True:
        output = csockid.recv(100)
        csockid.send(translate(output).encode('utf-8'))
    
   # Close the server socket
    ss.close()
    exit()

# translate str to ASCII as 1_2_3 for example
def translate(str):
    trans = ""
    for char in str:
        trans += ord(char) + "_"
    return trans.rstrip("_")