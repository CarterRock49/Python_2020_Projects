import turtle
down = int(-300)

for x in range(0,6):

    turtle.penup()
    turtle.goto(0,down)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    down = down + 100


