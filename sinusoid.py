import turtle
import math
import random

bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(10)

for i in range(2000):
	bob.forward(10)
	bob.left(math.sin(i/10)*25)
	bob.left(20)

turtle.done()