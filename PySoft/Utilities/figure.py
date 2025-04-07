import turtle
import time
screen = turtle.getscreen()
tortue = turtle.Turtle()
print("© Okmeque1 Software")
c = int(input("Please enter the amount of side lengths you want : "))

def option(a):
    angle = 360 / a
    for i in range(a):
        tortue.forward(50)
        tortue.right(angle)
        
    time.sleep(2)
    input("Press ENTER to EXIT...")
    tortue.clear()
option(c)
