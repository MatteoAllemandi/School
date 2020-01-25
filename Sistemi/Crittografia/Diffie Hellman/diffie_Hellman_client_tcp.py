import socket as sck
import random
import numpy as np

def isPrimo(n):
    for i in range(2, int(np.sqrt(n)) + 1, 2):
        if (n % i) == 0:
            return False
    return True

def main():
    #dichiarazione host e creazione oggetto socket
    HOST = "127.0.0.1"
    PORT = 1984
    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True:
        N = int(input("inserisci numero primo: "))
        if isPrimo:
            break

    while True:
        g = int(input("inserisci numero minore del precedente: "))
        if g<N:
            break

    a = random.randint(1,N)
    A = (g**a)%N

    #invio numero all'host con cui scambiare la chiave 
    s.send(str(A).encode())
    data = s.recv(4096)

    #ricezione numero dall'altro host 
    print("received -->" + str(data))
    B = int(data.decode())

    #chiusura socket
    s.close()

    #calcolo numero finale
    k = (B**a)%N
    print(f"il numero è {k}")

main()

