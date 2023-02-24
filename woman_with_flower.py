import turtle

# set up the turtle screen
screen = turtle.Screen()
screen.setup(800, 800)

# create a turtle instance
t = turtle.Turtle()

# set the pen size and color
t.pensize(3)
t.pencolor("black")

# draw the face
t.penup()
t.goto(0, -200)
t.pendown()
t.circle(200)

# draw the hat
t.penup()
t.goto(-200, 100)
t.pendown()
t.fillcolor("gray")
t.begin_fill()
t.circle(100, 180)
t.goto(0, 200)
t.goto(200, 100)
t.circle(100, 180)
t.end_fill()

# draw the flower
t.penup()
t.goto(0, 250)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.fillcolor("pink")
t.begin_fill()
for i in range(6):
    t.forward(30)
    t.left(60)
    t.forward(30)
    t.right(120)
t.end_fill()

# draw the eyes
t.penup()
t.goto(-70, 50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()
t.penup()
t.goto(70, 50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# draw the pupils
t.penup()
t.goto(-50, 60)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(50, 60)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

# draw the eyebrows
t.penup()
t.goto(-100, 100)
t.pendown()
t.goto(-20, 120)
t.goto(60, 100)

# draw the nose
t.penup()
t.goto(0, 0)
t.pendown()
t.goto(-20, -30)
t.goto(20, -30)

# draw the lips
t.penup()
t.goto(-70, -80)
t.pendown()
t.setheading(-60)
t.circle(70, 120)

# keep the screen open until it's manually closed
turtle.done()
