import turtle
import time
screen = turtle.getscreen()
tortue = turtle.Turtle()
c = int(input("Please enter number above 3 : "))
print("Creator = Okmeque1")

def option(a):
    angle = 360 / a
    for i in range(a):
        tortue.forward(50)
        tortue.right(angle)
        
    time.sleep(2)
    tortue.clear()
for z in range(3,c):
    option(z)
