import turtle
import random

direction_list = []
passo=15
gradi=90
turtle.color("red","blue")
turtle.speed(1)

for k in range(50):
    number=random.random()

    if (number <= 0.25):
        direction_list +="f"
    elif (number >0.25 and number <=0.5):
        direction_list +="b"
    elif (number >0.5 and number <=0.75):
        direction_list += "l"
    else:
        direction_list += "r"

for k in direction_list:
    if (k =="f"):
        turtle.forward(passo)
    elif (k =="b"):
        turtle.back(passo)
    elif (k =="l"):
        turtle.left(gradi)
    else:
        turtle.right(gradi)
turtle.done()
