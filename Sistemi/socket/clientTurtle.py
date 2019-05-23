import socket as sck

HOST = "127.0.0.1"
PORT = 50000

STOP = "stop"

s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
    cmd = input("inserisci comando tartaruga: --> ")

    s.send(cmd.encode())

    if(cmd == "stop"):
        break

s.close()
print("chiusura connessione")

