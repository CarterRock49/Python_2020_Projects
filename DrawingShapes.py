import turtle
#variables
pen_color = str()
fill_color = str()
pen_size = int()
shape = str()
loc = str()

loc = input("Please enter a location, topleft, topright, bottomleft, or bottomright: ")
shape = input("Please enter square or circle: ")

if shape == "square":
    fill_color = input("Please enter choose a fill color, red, blue, or yellow: ")
    if fill_color == "red":
        pen_color = "purple"
        if loc == "topleft":
            pen_size = 3
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "topright":
            pen_size = 5
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "bottomleft":
            pen_size = 7
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "bottomright":
            pen_size = 9
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        else:
            print("You didn't enter a choice correctly")
    elif fill_color == "blue":
        pen_color = "green"
        if loc == "topleft":
            pen_size = 3
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "topright":
            pen_size = 5
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "bottomleft":
            pen_size = 7
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "bottomright":
            pen_size = 9
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        else:
            print("You didn't enter a choice correctly")

    elif fill_color == "yellow":
        pen_color = "olive"
        if loc == "topleft":
            pen_size = 3
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "topright":
            pen_size = 5
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "bottomleft":
            pen_size = 7
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        elif loc == "bottomright":
            pen_size = 9
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.end_fill()
        else:
            print("You didn't enter a choice correctly")

    else:
        print("You didn't enter a choice correctly")
elif shape == "circle":
    pen_color = input("Please enter choose a pen color, red, blue, or yellow: ")
    if pen_color == "red":
        fill_color = "purple"
        if loc == "topleft":
            pen_size = 3
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "topright":
            pen_size = 5
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "bottomleft":
            pen_size = 7
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "bottomright":
            pen_size = 9
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        else:
            print("You didn't enter a choice correctly")
    elif pen_color == "blue":
        fill_color = "green"
        if loc == "topleft":
            pen_size = 3
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "topright":
            pen_size = 5
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "bottomleft":
            pen_size = 7
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "bottomright":
            pen_size = 9
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        else:
            print("You didn't enter a choice correctly")
    elif pen_color == "yellow":
        fill_color = "olive"
        if loc == "topleft":
            pen_size = 3
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "topright":
            pen_size = 5
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, 250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "bottomleft":
            pen_size = 7
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(-250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        elif loc == "bottomright":
            pen_size = 9
            turtle.pensize(pen_size)
            turtle.pencolor(pen_color)
            turtle.fillcolor(fill_color)
            #moving the pen
            turtle.penup()
            turtle.goto(250, -250)
            turtle.pendown()
            #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
        else:
            print("You didn't enter a choice correctly")
    else:
        print("You didn't enter a choice correctly")
else:
    print("You didn't enter a choice correctly")

