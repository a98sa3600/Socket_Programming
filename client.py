import socket
import threading

HEADER = 64 # fixed length header iof what we're gonna call 64bytes
PORT = 5050
SERVER = "192.168.1.102"
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# AF_INET:IPv4  SOCK_STREAM:TCP SOCK_DGRAM:UDP
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '* (HEADER-len(send_length)) # make sure message length is 64bytes
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

    
    
send("Hello World1")
input()
send("Hello World2")
input()
send("Hello World3")
input()
send("Hello World4")
send(DISCONNECT_MESSAGE)
send("Hello World test")
