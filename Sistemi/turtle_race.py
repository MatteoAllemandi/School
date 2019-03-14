import turtle 
import random

WIDTH=800           #global variables setup
HEIGHT=600
XSTART=-WIDTH/2
MAXRAND=30
GRADES=90
MULTIPLIER=2       #the higher will be the multiplier,the less space will be between turtles
toggle,cont=0,1

turtle.title("GARE CLANDESTINE DI TARTARUGHE")

def calculateY(padding,toggle,cont):        #function to calculate Y value of each turtle

    origin = 0

    if toggle==0:
        y=origin + padding*cont
        toggle = 1
    else:
        y=origin - padding*cont
        toggle = 0
    
    cont+=1

    return y,toggle,cont

def forward(vector,players):                #function to calculate the distance that each turtle will ride 
    cont=0
    stop=False
    while True:
        for i in vector:
            if i.xcor() >= WIDTH//2:
                vincitore=cont
                stop=True
                i.color("red","red")
                break
            i.forward(random.randrange(0,MAXRAND+1))
            cont+=1
        
        if stop:
            break

    return (cont%int(players))


def drawContours():                 #function to draw the start and arrive lines
    drawer=turtle.Turtle()
    drawer.speed(0)
    drawer.up()
    drawer.goto(XSTART,-HEIGHT/2)
    drawer.down()
    drawer.left(GRADES)
    drawer.forward(HEIGHT)
    drawer.up()
    drawer.goto(WIDTH/2,-HEIGHT/2)
    drawer.down()
    drawer.forward(HEIGHT)
    drawer.hideturtle()



number=input("inserisci il numero di partecipanti: ")
#number="10"
vector = []
padding=HEIGHT//(int(number)*MULTIPLIER)     #distance for the first turtle from the origin (0), will be used to calculate y coordinate

drawContours()

for i in range(0,int(number)):
    vector.append(turtle.Turtle())

for i in vector:                                        #setup in the start position for each turtle 
    i.penup()
    i.speed(10)
    y,toggle,cont = calculateY(padding,toggle,cont)
    i.goto((XSTART),y)

vincitore=forward(vector,number)

print("ha vinto la tartaruga con indice " + str(vincitore))     

turtle.done()



