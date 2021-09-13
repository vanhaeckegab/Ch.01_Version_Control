import turtle
ed = turtle.Turtle()
screen = turtle.Screen()  # makes a screen object
screen.setup(1000, 1000)

ed.pensize(200)  # width of pen line
ed.speed(10)  # speed of drawing. Go fast to not waste time.
ed.penup()
ed.color("black")
ed.goto(-200, 150)
ed.pd()
ed.right(90)
ed.fd(200)
ed.pu()
ed.pu()

ed.pensize(150)
ed.color("red")
ed.goto(-200, 150)
ed.pd()
ed.fd(200)
ed.pu()

ed.pensize(450)
ed.color("black")
ed.goto(0, 150)
ed.pd()
ed.fd(125)
ed.pu()

ed.pensize(400)
ed.color("orangered")
ed.goto(0, 150)
ed.pd()
ed.fd(125)
ed.pu()

ed.pensize(150)
ed.goto(-150, 0)
ed.color("black")
ed.pd()
ed.fd(225)
ed.pu()

ed.pensize(100)
ed.goto(-150, 0)
ed.color("orangered")
ed.pd()
ed.fd(225)
ed.pu()

ed.pensize(150)
ed.goto(150, 0)
ed.color("black")
ed.pd()
ed.fd(225)
ed.pu()

ed.pensize(100)
ed.goto(150, 0)
ed.color("orangered")
ed.pd()
ed.fd(225)
ed.pu()

ed.pensize(400)
ed.color("orangered")
ed.goto(0, 150)
ed.pd()
ed.fd(125)
ed.pu()

ed.pensize(250)
ed.goto(100, 150)
ed.pd()
ed.color("black")
ed.left(90)
ed.fd(100)
ed.pu()

ed.pensize(200)
ed.goto(100, 150)
ed.pd()
ed.color("dark grey")
ed.fd(100)
ed.pu()

ed.pensize(75)
ed.goto(175, 175)
ed.pencolor("light grey")
ed.pd()
ed.forward(50)

ed.penup()
ed.goto(200, -350)
ed.color("black")
ed.write('Gabe Van Haecke', font=("Arial", 16, "normal"))  # signs your name to your art
turtle.exitonclick()  # Keeps pycharm window open so we can see the drawing
