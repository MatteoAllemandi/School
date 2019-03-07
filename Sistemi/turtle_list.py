import turtle
import random

direction_list = []
passo=15
gradi=90
turtle.color("red","blue")
turtle.speed(1)

for k in range(50):
    if (random.random()<=0.25):
        direction_list +="f"
    elif (random.random()>0.25 and random.random() <=0.5):
        direction_list +="b"
    elif (random.random()>0.5 and random.random() <=0.75):
        direction_list += "l"
    else:
        direction_list += "r"

for k in range(len(direction_list)):
    if (direction_list[k]=="f"):
        turtle.forward(passo)
    elif (direction_list[k]=="b"):
        turtle.back(passo)
    elif (direction_list[k]=="l"):
        turtle.left(gradi)
    else:
        turtle.right(gradi)
turtle.done()