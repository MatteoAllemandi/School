import math

graph = [
    [0,3,0,4],
    [3,0,1,5],
    [0,1,0,2],
    [4,5,2,0]]

source = 0
nodeNumber = len(graph)

labelList = [math.inf for i in range(nodeNumber)]
labelList[source] = 0

unexploredNodes = [i for i in range(nodeNumber)]

while len(unexploredNodes)>0:
    
    print(unexploredNodes)

    minLabel = min([labelList[node] for node in unexploredNodes])

    for i in unexploredNodes:
        if labelList[i] == minLabel:
            currentNode = i
        else:
            break

    print(currentNode)
    unexploredNodes.remove(currentNode)

    for neighbourNode,weight in enumerate(graph[currentNode]):
        if weight>0:
            distance = labelList[currentNode]+weight
            if(distance<labelList[neighbourNode]):
                labelList[neighbourNode]=distance

print(labelList)
    