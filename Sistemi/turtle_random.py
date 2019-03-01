import turtle 
import random

print("inserisci numero di spostamenti: ")
num=input()

MOLT=25
passo=1
k=0

for k in range(int(num)):
    if((random.random()*10)<5):
        turtle.left(90)
        turtle.forward(passo*25)
    else:
        turtle.right(90)
        turtle.forward(passo*25)
  
turtle.done()