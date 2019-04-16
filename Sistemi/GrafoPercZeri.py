import math
import random

dim = int(input("inserisci dimensione matrice: "))
percZeri = int(input("inserisci percentuale di zeri: "))
numZeri = (((dim**2)*percZeri)//100)

graph = [[math.inf]*dim]*dim
cntZeri = 0
MAX_LUNG = 20


for r in range(dim):
    for c in range(dim):
        graph[r][c] = random.randrange(1,MAX_LUNG)
    #print("aggiunto " + str(graph[r][c]))

print("originale---> " + str(graph))

while True:
    r = random.randrange(0,dim)
    c = random.randrange(0,dim)

    if graph[r][c] == 0:
        cntZeri += 1
    else:
       graph[r][c] = 0 
       cntZeri +=1
    
    if(cntZeri >numZeri):
        break

print("modifica----> " + str(graph))