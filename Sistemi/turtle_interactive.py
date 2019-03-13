import turtle
import random
import time 

passo=15
gradi=90
turtle.color("red","blue")
turtle.speed(1)

while(True) :
    print("inserisci un comando (f/b/l/r) oppure q per uscire: ")
    com=input()

    if (com == "f"):
        turtle.forward(passo)
    elif (com == "b"):
        turtle.back(passo)
    elif (com == "l"):
        turtle.left(gradi)
    elif (com == "r"):
        turtle.right(gradi)
    elif (com == "q"):
        break
    else:
        print("comando inesistente")

#turtle.done()      #toggle comment for the permanent turtle screen after exit with 'q' 
time.sleep(2)
turtle.Screen.bye() #close the turtle screen after exit
