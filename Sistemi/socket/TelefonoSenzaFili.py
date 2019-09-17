import socket as socket

IP_SERVER = "192.168.10.53"
PORT_SERVER = 8080

IP_CLIENT = "192.168.10.54"
PORT_CLIENT = 8080

STOP = "stop"

socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_server.bind((IP_SERVER,PORT_SERVER))

socket_client.connect((IP_CLIENT,PORT_CLIENT))


socket_server.listen()

conn, addr = socket_server.accept()
print("connected to " + str(addr))


while True:
    data = conn.recv(4096)
    print("received: --> " + str(data))

    if data==STOP.encode() :
        break

    socket_client.send(data)

socket_client.close()
socket_server.close()