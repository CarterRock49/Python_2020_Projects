import turtle
import time
import random
'''
#variables
horizontal = int()
radius = int()
colors = ["red", "blue", "yellow", "green"]
pen_size = int()
colors[1]
horizontal = -200
radius = 25
pen_size = 2
#Initialize the pensize by typing in
turtle.pensize(5)
#loop to draw the circles
for count in range(0, 4):
    #set the pen size and fill color
    turtle.fillcolor(colors[count])
    turtle.pensize(pen_size)
    turtle.begin_fill()
    #draw circle
    turtle.circle(radius)
    #reset location, radius and pen size
    horizontal = horizontal + 75
    radius = radius + 20
    pen_size = pen_size + 2
    #moving the turtle
    turtle.penup()
    turtle.goto(horizontal, 0)
    turtle.pendown()
    turtle.end_fill()
'''
#varibles
pen_size = int()
radius = int()
colors = ["red", "blue", "yellow", "green"]
hor = int()
vrt = int()
col = int()
#text
turtle.setup(600, 600)
turtle.write('Ready for more circles?', font=('Times New Roman', 16, 'bold'), align='center')
time.sleep(3)
turtle.clear()
#loop
for x in range(0, 20):
    #get random numbers
    col = random.randint(0, 3)
    radius = random.randint(25, 125)
    vrt = random.randint(-150, 150)
    hor = random.randint(-150, 150)
    pen_size = random.randint(0, 10)
    #moving the turtle
    turtle.penup()
    turtle.goto(hor, vrt)
    turtle.pendown()
    #set the pen size and fill color
    turtle.fillcolor(colors[col])
    turtle.pensize(pen_size)
    #draw circle
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()