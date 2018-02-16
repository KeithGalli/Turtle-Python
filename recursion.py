import turtle

bob = turtle.Turtle()
bob.getscreen().bgcolor("#994444")
bob.penup()
bob.goto((-200,100))
bob.pendown()

def star(turtle, size):
	if size <= 10:
		return
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/3)
			turtle.left(216)
		turtle.end_fill()

star(bob, 360)

turtle.done()

