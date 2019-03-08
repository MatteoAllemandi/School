import turtle
import random

passo=15
gradi=90
turtle.color("red","blue")
turtle.speed(1)

while(True) :
    print("comando(f/b/l/r): ")
    com=input()

    if (com=="f"):
        turtle.forward(passo)
    elif (com=="b"):
        turtle.back(passo)
    elif (com=="l"):
        turtle.left(gradi)
    elif (com=="r"):
        turtle.right(gradi)
    else:
        print("comando inesistente")
    
turtle.done()
