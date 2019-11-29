'''Matteo Allemandi RSA in python'''
import math
import random

def mcm(n1,n2):                             #trova minimo comune multiplo
    return int((n1*n2)/math.gcd(n1,n2))

def trovaC(m):                  #trova un numero compreso fra 2 ed m che abbia il massimo comune divisore uguale ad 1
    for c in range(2,m):
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

def decodifica(lc,d,n):     #ðecodifica del numero codificato 
    return ((lc**d)%n)

p = 5
q = 11

n=p*q     
m = mcm(p-1,q-1)
c = trovaC(m)

if c == -1:
    print("errore")
    exit(0)
else:
    d = trovaD(c,m)
    print(f"n-->{n}\nc --> {c}\nd--> {d}\nm--> {m}\n")

l = 12
print(f"lettera da codificare ---> {l}")

lc = codifica(l,c,n)
print(f"lettera codificata ---> {lc}")




