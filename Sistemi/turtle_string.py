import turtle
import random

print("inserisci le indicazioni per la tartaruga: ")        #input for turtle's path
dir=input()

passo=10                    #set speed,distance for each forward and color
turtle.speed(1)
turtle.color("red","blue")

for k in range(len(dir)):
    if(dir[k] == "f"):
        turtle.forward(passo)
    elif dir[k] == "r":
        turtle.right(90)
    elif dir[k] == "l":
        turtle.left(90)
    else:
        turtle.back(passo)

turtle.done()