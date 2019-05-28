import socket as sck 

HOST,PORT = "127.0.0.1","1984"

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,5000))

while True:
    testo = input("inserisci il messaggio: ")
    s.sendto(testo.encode(),HOST)

    data,server = s.recvfrom(4096)
    print("ricevuto --> " + str(data) + "from --> " + str(server))

    if(str(data) == "stop"):
        break

s.close()
print("socket chiuso")

