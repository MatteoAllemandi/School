import socket as sck

HOST = "127.0.0.1"
PORT = 50007

STOP = "stop"

s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print("connected to " + str(addr))

while 1:
    data = conn.recv(4096)
    print("received: --> " + str(data))
    conn.send(data)
    if not data: break
    if data==STOP.encode() :
        break

conn.close()
