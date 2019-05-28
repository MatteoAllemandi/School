import socket as sck 

HOST,PORT = "127.0.0.1","1984"

s = sck.socket(sck.AF_INET,sck.SOCK_DGRAM)
s.bind((HOST,5000))

while True:
    data,address = s.recvfrom(4096)
    print("ricevuto --> " + str(data) + " da " + str(address))

    if(str(data) == "stop"):
        break

    text = input("inserisci risposta: ")
    s.sendto(text.encode(),HOST)
    
s.close()
print("chiusura server")