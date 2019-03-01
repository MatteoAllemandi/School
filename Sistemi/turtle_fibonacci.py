import turtle       #import of the turtle library

n1=0            
n2=1
somma=0
COEFF=25
k=0 

print("inserisci il numero di bracci da disegnare: ")  #request of numbers
nCicl=input()
print(int(nCicl))

while k in range(int(nCicl)):
    somma=n1+n2
    n1=n2           #sums for fibonacci's sequence
    n2=somma

    turtle.forward(n2*COEFF)        #forward for n2 distance
    turtle.left(90)                 #turn left of 90 degrees
    turtle.forward(somma*COEFF)
    turtle.left(90)
    
    k=k+1 

turtle.done()
