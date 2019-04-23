import math

'''
Funzione per calcolare dizionario delle adiacenze
def adj_dict(graph):
    adj_dictionary = {}
    nodo = -1

    for i in graph:
        cont=0
        nodo +=1
        confinanti = []

        for k in i:
            if(k != 0):
                confinanti.append(cont)
            cont +=1

        adj_dictionary[str(nodo)] = confinanti

    return adj_dictionary  
'''

adj_dict={  0:[1,2],
            1:[0,5],
            2:[0,3],
            3:[2,4,5],
            4:[3,6,7],
            5:[1,3],
            6:[4,7],
            7:[4,6]}  

def dijkstra(graph,initial,finish,dim):
    labelList = [math.inf] * len(graph) #inizializzazione delle label (moltiplico per il numero di nodi per le righe)
    labelList[initial] = 0                    #distanza dal nodo sorgente = 0
    unexploredNode = []   #nodi da esplorare

    for cont in range(dim):
        unexploredNode.append(cont)

    cntPasso=0

    while len(unexploredNode)>0:
        #print("Passo numero: %d"% cntPasso)
        #print("Nodi inesplorati: ", unexploredNode)
        #print("Lista delle label: ", labelList)
        #print("-----------------------------------------------")
        #scelgo il nodo con label minore(k)
        infiniteList = [math.inf] * len(graph)
        
        for i in unexploredNode:
            infiniteList[i]=labelList[i]    #valore della labelList[i] 
        
        minimun = min(infiniteList)   #trovo il minimo

        if(minimun==math.inf):  #controllo per uscire dal ciclo
            break
        
        currentNode = infiniteList.index(minimun)  #prendo l'indice del valore minimo
        for node, weight in enumerate(graph[currentNode]):       #ciclo for con ricerca dei nodi collegati a k per indici non ancora esplorati
            if(weight!=0):   #verifico che sia collegato e che non sia se stesso
                newLabel = labelList[currentNode] + weight
                if(newLabel<labelList[node]):
                    labelList[node] = newLabel     #per ogni nuovo nodo sommo (valore label(k)+peso arco di quel nodo) il valore della sua label e controllo se sono minori così sostituisco sennò niente
        
        cntPasso=cntPasso+1
        unexploredNode.remove(currentNode) #rimuovo l'indice visitato

    print("la distanza dal nodo %s di partenza ed il nodo %s di arrivo e' --> %s" % (initial,finish,labelList[finish]))
    
    return labelList

def generateGraph(adj_dict):
    nodeNumber=0
    graph=[]
    for key,value in adj_dict.items():      #stampo il dizionario
        print("%s --> %s" %(key,value))
        nodeNumber+=1
    
    #graph = [[False]*nodeNumber]*nodeNumber

    graph = [[False for r in range(nodeNumber)] for c in range(nodeNumber)] #inizializzo la matrice a false
    
    for key,value in adj_dict.items():
        for k in value:
            graph[key][k] = True        #scorrendo la ista assegno true alle celle dei nodi collegati fra loro così da creare l grafo

    return graph,nodeNumber


start = int(input("inserire il nodo di partenza: "))
finish = int(input("inserire il nodo di arrivo: "))

graph,dim = generateGraph(adj_dict)

dijkstra(graph,start,finish,dim)
#print(graph)
