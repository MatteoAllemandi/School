'''Matteo Allemandi RSA in python'''
import math
import random
import numpy as np 

def isPrime(n):                             #controlla se il numero è primo 
    for p in range(2, int(np.sqrt(n)) + 1):
        if (n % p == 0):
            return False
    return True

def mcm(n1,n2):                             #trova minimo comune multiplo
    return int((n1*n2)/math.gcd(n1,n2))

def trovaC(m):                  #trova un numero compreso fra 2 ed m che abbia il massimo comune divisore uguale ad 1
    for c in range(m,2,-1):
        if(math.gcd(c,m) == 1):
            break
    return c

def trovaD(c,m):                #trova un numero compreso fra 0 ed m il cui modulo del prodotto con il C precedentemente trovato sia uguale ad 1 
    for d in range(0,m):
        if ((c*d)%m == 1):
            break
    return d

def codifica(l,c,n):        #codifica del numero da inviare 
    return ((l**c)%n)

def decodifica(lc,d,n):     #Decodifica del numero codificato 
    return ((lc**d)%n)

def main():
    prime=False

    while prime==False:
        p = int(input("inserisci numero P: "))
        prime = isPrime(p)

    prime = False

    while prime==False:
        q = int(input("inserisci numero Q: "))
        prime = isPrime(q)

    n=p*q                   #trovo N
    m = mcm(p-1,q-1)        #trovo M
    c = trovaC(m)           #chiamata alla funzione per trovare C

    if c == -1:             #se C non viene trovato, termina il programma
        print("errore")
        exit(0)
    else:
        d = trovaD(c,m)
        print(f"n-->{n}\nc --> {c}\nd--> {d}\nm--> {m}\n")

    l = 12
    print(f"lettera da codificare ---> {l}")        

    lc = codifica(l,c,n)
    print(f"lettera codificata ---> {c}")       #codifica la lettera usando le chiavi trovate   

    #print(str(decodifica(lc,d,n))) stampa eventuale decodifica della lettera

main()
