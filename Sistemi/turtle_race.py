import turtle 
import random

WIDTH=600       #global variables setup
HEIGHT=500
XSTART=-WIDTH/2
MAXRAND=20
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
            #i.pendown()
            if i.xcor() >= WIDTH//2:
                vincitore=cont
                stop=True
                vector.pop(vincitore%int(players))
                #i.color("red","red")
                break
            i.forward(random.randrange(0,MAXRAND+1))
            cont+=1
        
        if stop:
            for i in vector:
                i.clear()
                i.hideturtle()
            break

    return (cont%int(players))


def drawContours():                 #function to draw the start and arrive lines
    drawer=turtle.Turtle()
    #drawer.speed(0)
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



#number=input("inserisci il numero di partecipanti: ")
number="13"
vector = []
turtle.colormode(255)
padding=HEIGHT//(int(number)*MULTIPLIER)     #distance for the first turtle from the origin (0), will be used to calculate y coordinate

drawContours()

for i in range(0,int(number)):
    vector.append(turtle.Turtle())

for i in vector:  
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    i.color((b,g,r))                                      #setup in the start position for each turtle 
    i.penup()
    i.speed(6)
    y,toggle,cont = calculateY(padding,toggle,cont)
    i.goto((XSTART),y)

vincitore=forward(vector,number)

print("ha vinto la tartaruga con indice " + str(vincitore))     

turtle.done()
