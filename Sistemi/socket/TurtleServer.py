import socket as socket
import turtle as turtle

HOST = "127.0.0.1"
PORT = 50000

STOP = "stop"

print("inserisci un comando (f/b/l/r) e guarda lo spostamento del cursore")

passo=15
gradi=90

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print("connesso a --> " + str(addr))

while 1:
    data = conn.recv(4096)

    if (data.decode() == "f"):
        turtle.forward(passo)
    elif (data.decode() == "b"):
        turtle.back(passo)
    elif (data.decode() == "l"):
        turtle.left(gradi)
    elif (data.decode() == "r"):
        turtle.right(gradi)
    elif (data.decode() == "stop"):
        break
    else:
        pass

    if not data: break
    if data==STOP.encode() :
        break

turtle.Screen.bye()
conn.close()
