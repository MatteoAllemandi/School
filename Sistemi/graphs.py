m=[[0,1,0,1,0],[1,0,1,1,1],[0,1,0,1,0],[1,1,1,0,0],[0,1,0,0,0]]

nodo = -1

for i in m:

    cont=0
    nodo +=1
    confinanti = []

    for k in i:
        if(k==1):
            confinanti.append(cont)
        cont +=1

    print("nodo: -> " + str(nodo) + "--->" + str(confinanti))
    
    


    
    
