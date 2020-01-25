import socket as sck
import random
import numpy as np

def isPrimo(n):
    for i in range(2, int(np.sqrt(n)) + 1, 2):
        if (n % i) == 0:
            return False
    return True

def main():
    HOST = "127.0.0.1"      #dichiarazione host ed oggetto socket, quindi creazione server
    PORT = 1984
    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(1)

    while True:
        N = int(input("inserisci numero primo: "))      #controllo che il primo dei due numeri dell'algoritmo sia primo
        if isPrimo:
            break

    while True:
        g = int(input("inserisci numero minore del precedente: "))  #controllo che il secondo numero sia inferiore al primo
        if g<N:
            break

    b = random.randint(1,N)
    B = (g**b)%N

    #connessione 
    conn, addr = s.accept()
    print("connected to " + str(addr))

    #ricezione dati e conversione
    data = conn.recv(4096)
    print("received: --> " + str(data))
    A = int(data.decode())

    #invio dati calcolati
    conn.send(str(B).encode())
    conn.close()

    #calcolo del risultato finale
    k=(A**b)%N
    print(f"il numero è {k}")

main()
