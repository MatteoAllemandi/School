import socket as sck

HOST = "0.0.0.0" #"192.168.10.68"
PORT = 1984

STOP = "stop"

s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn, addr = s.accept()
print("connected to " + str(addr))

while 1:
    data = conn.recv(4096)
    print("received: --> " + str(data))

    if not data: break
    if data==STOP.encode() :
        break

    testo = input("inserisci stringa: ")
    conn.send(testo.encode())


conn.close()
