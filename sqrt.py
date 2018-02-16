import turtle
import math
import random

bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(10)

for i in range(2000):
	bob.forward(math.sqrt(i))
	bob.left(i%180)

turtle.done()