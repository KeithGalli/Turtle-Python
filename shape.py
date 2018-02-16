import turtle

bob = turtle.Turtle()

bob.color("blue", "cyan")

# Square
bob.begin_fill()
bob.forward(100)
bob.setheading(90)
bob.forward(100)
bob.setheading(180)
bob.forward(100)
bob.setheading(270)
bob.forward(100)
bob.end_fill()

bob.penup()
bob.setheading(270)
bob.forward(120)
bob.pendown()

bob.begin_fill()
bob.setheading(0)
bob.forward(100)
bob.setheading(90)
bob.forward(100)
bob.setheading(180)
bob.forward(100)
bob.setheading(270)
bob.forward(100)
bob.end_fill()

turtle.done()