"""
All code written by Carter Rock
Decomposition 
import tools required
declare four functions
call main function
within the main function
set window size
call functions in required order consecutively 
in shape function
ask user for desired shape
return desired shape
in location fuction
declare varibles
declare array
single loop to input random varibles into array
return array
in color and printing fuction
declare color list
user input for color selection
declare varibles
multi-alternative IF structure with nested loops inside to print at array locations in various shapes
"""
import turtle
import time
import random

#All code written by Carter Rock
#function to choose shape for later
def shape():
    #user input for instructure later and returning that input
    shapekind = input("Please choose a shape (S)quare or (C)ircle, (T)riangle")
    return shapekind

#All code written by Carter Rock
#function to declare array and get random locations
def loc():
    #declare varibles
    shapelist = [[0,0],[0,0],[0,0],[0,0]]
    hor = int()
    vrt = int()
    first = int(0)
    second = int(0)
    #single to get random locations for the array
    for index in range(len(shapelist)):
        vrt = random.randint(-500, 500)
        hor = random.randint(-500, 500)
        shapelist[first][second] = vrt
        second = second + 1
        shapelist[first][second] = hor
        first = first + 1
        second = 0
    return shapelist

#All code written by Carter Rock
#function for color selection and drawing the shapes
def color(switchshape, randomloc):
    #list for color selection
    colors = ["red", "blue", "yellow", "orange", "green"]
    #input to select color
    x = int(input("Enter a number to select a color: 0.red 1.blue 2.yellow 3.orange 4.green"))
    turtle.pencolor(colors[x])
    turtle.fillcolor(colors[x])
    turtle.pensize(5)
    #declare varibles
    temp = int()
    temp2 = int()
    index2 = int(0)
    #multi-alternative IF structure with nested loops inside to print at array locations
    if (switchshape == "S"):
        for index in range(len(randomloc)):
            #setting location
            temp1 = randomloc[index][index2]
            for index2 in range(len(randomloc[index])):
                #setting location
                temp2 = randomloc[index][index2]
                turtle.penup()
                turtle.goto(temp1, temp2)
                turtle.pendown()
                #drawing shape
            turtle.begin_fill()
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.end_fill()
    elif (switchshape == "C"):
        for index in range(len(randomloc)):\
            #setting location
            temp1 = randomloc[index][index2]
            for index2 in range(len(randomloc[index])):
                #setting location
                temp2 = randomloc[index][index2]
                turtle.penup()
                turtle.goto(temp1, temp2)
                turtle.pendown()
                #drawing shape
            turtle.begin_fill()
            turtle.circle(50)
            turtle.end_fill()
    elif (switchshape == "T"):
        for index in range(len(randomloc)):
            #setting location
            temp1 = randomloc[index][index2]
            for index2 in range(len(randomloc[index])):
                #setting location
                temp2 = randomloc[index][index2]
                turtle.penup()
                turtle.goto(temp1, temp2)
                turtle.pendown()
                #drawing shape
            turtle.begin_fill()
            turtle.forward(100)
            turtle.left(120)
            turtle.forward(100)      
            turtle.left(120)
            turtle.forward(100)
            turtle.left(120)
            turtle.end_fill()
    else:
        print("Something is wrong here")

#All code written by Carter Rock
def main():
    #setting up turtle
    turtle.setup(1200, 1000)
    turtle.shape('turtle')
    #calls function
    returnshape = shape()
    returnloc = loc()
    color(returnshape, returnloc)



main()


