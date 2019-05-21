import socket as sck

HOST="127.0.0.1"
PORT=50007

s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    testo = input("inserisci stringa:  ")
    if(testo=="stop"):
        break
    s.send(testo.encode())
    data = s.recv(4096)

s.close()

print("chiusura server")
