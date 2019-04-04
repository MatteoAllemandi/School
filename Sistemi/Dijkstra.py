import math

grafo = [[0,1,4,0,0,0,0,0],
         [1,0,0,0,0,2,0,0],
         [4,0,0,5,0,0,0,0],
         [0,0,5,0,1,3,0,0],
         [0,0,0,1,0,0,2,3],
         [0,2,0,3,0,0,0,0],
         [0,0,0,0,2,0,0,4],
         [0,0,0,0,3,0,4,0]]

labelList = [math.inf] * len(grafo) #inizializzazione
labelList[0] = 0    #distanza da nodo sorgente uguale a 0

nodiDaEsplorare = [0,1,2,3,4,5,6,7]

while len(nodiDaEsplorare)>0:
    cont = 0
    near_list = []
    k = min(labelList)

    for i in labelList[k]:
        if(i!=0):
            near_list.append(cont)
        cont+=1

    for i in labelList:
        
    
    # Scelgo il nodo che ha la label più piccola (k).
    # Ricerco i nodi collegati al nodo k -> ciclo for sulla riga k di grafo
    # per ogni nodo sostituisco il valore(label di k + peso dell'arco verso nodo vicino)
    # della label SOLO se minore di quello presente.
    # 