import turtle
import random

print("inserisci le indicazioni per la tartaruga(f/b/l/r): ")        #input for turtle's path
dir=input()

passo=10                    #set speed,distance for each forward and color
turtle.speed(1)
turtle.color("red","blue")

for k in dir:
    if(k == "f"):
        turtle.forward(passo)
    elif k == "r":
        turtle.right(90)
    elif k == "l":
        turtle.left(90)
    else:
        turtle.back(passo)

turtle.done()
