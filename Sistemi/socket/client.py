import socket as sck

HOST = "192.168.10.58"
PORT = 1984

s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:

    testo = input("inserisci stringa:  ")
    s.send(testo.encode())

    if(testo=="stop"):
        break

    data = s.recv(4096)
    print("received -->" + str(data))

s.close()

print("chiusura server")
