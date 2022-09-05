import turtle
import random
import time
#initializing global variables
#While global variables are generally discouraged, due to how the turtle onkeypress events work, Global variables are one of the only and by far simpliest way to make this work.
#Without global variables this program would haver been a lot more complicated to make.
timeint = 0
previousint = 0
right = False
left = False
gamestart = False
started = False
bulletmove = True
score = 0
lasthit = 0
killcount = 0
#creating turtles
mainblock = turtle.Turtle()
bullet = turtle.Turtle()
scorewriter = turtle.Turtle()
def placeblocks():#places all of the breakable blocks
    global allblocks
    blocks = []
    blocks2 = []
    blocks3 = []
    blocks4 = []
    blocks5 = []
    blocks6 = []
    blockspeed = 8
    xpostion = -250
    for index in range(0,11):#fills up bottom row
        blocks.append(turtle.Turtle())
        blocks[index].shape('square')
        blocks[index].speed(blockspeed)
        blocks[index].shapesize(.5,2)
        blocks[index].penup()
        blocks[index].setpos(xpostion,150)
        xpostion = xpostion + 50
    xpostion = -250
    for index in range(0,11):#fills up second row
        blocks2.append(turtle.Turtle())
        blocks2[index].shape('square')
        blocks2[index].speed(blockspeed)
        blocks2[index].shapesize(.5,2)
        blocks2[index].penup()
        blocks2[index].setpos(xpostion,175)
        xpostion = xpostion + 50

    xpostion = -250#fills up third row
    for index in range(0,11):
        blocks3.append(turtle.Turtle())
        blocks3[index].shape('square')
        blocks3[index].speed(blockspeed)
        blocks3[index].shapesize(.5,2)
        blocks3[index].penup()
        blocks3[index].setpos(xpostion,200)
        xpostion = xpostion + 50

    xpostion = -250
    for index in range(0,11):#fills up fourth row
        blocks4.append(turtle.Turtle())
        blocks4[index].shape('square')
        blocks4[index].speed(blockspeed)
        blocks4[index].shapesize(.5,2)
        blocks4[index].penup()
        blocks4[index].setpos(xpostion,225)
        xpostion = xpostion + 50

    xpostion = -250
    for index in range(0,11):#fills up fifth row
        blocks5.append(turtle.Turtle())
        blocks5[index].shape('square')
        blocks5[index].speed(blockspeed)
        blocks5[index].shapesize(.5,2)
        blocks5[index].penup()
        blocks5[index].setpos(xpostion,250)
        xpostion = xpostion + 50

    xpostion = -250
    for index in range(0,11):#fills up sixth row
        blocks6.append(turtle.Turtle())
        blocks6[index].shape('square')
        blocks6[index].speed(blockspeed)
        blocks6[index].shapesize(.5,2)
        blocks6[index].penup()
        blocks6[index].setpos(xpostion,275)
        xpostion = xpostion + 50
    allblocks = [blocks,blocks2,blocks3,blocks4,blocks5,blocks6]#putting all of the lists into one list for easier access outside of this function. Called with allblocks[x][y]
def quit(): #runs when q is pressed to quit game
    print("Quiting...")
    gameend("offscreen")
def gameend(end):#ends the game. say you win or lose based on how the game ended
    global score
    #backdrop and backdrop2 are used to make a box behind the text
    backdrop2 = turtle.Turtle()
    backdrop2.penup()
    backdrop2.shape("square")
    backdrop2.shapesize(4.5,5.5)
    backdrop = turtle.Turtle()
    backdrop.penup()
    backdrop.shape("square")
    backdrop.shapesize(4,5)
    backdrop.color("white")
    backdrop.setpos(0,0)
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    global gamestart
    gamestart = False
    writer.setpos([-47,20])
    writer.write("GAME OVER",font=('Arial', 9, 'normal'))
    writer.setpos([-47,-10])
    writer.write("Your Score: "+str(score),font=('Arial', 9, 'normal')) 
    if end == "offscreen":#when ball goes off the bottom of the screen
        writer.setpos([-47,-30])
        writer.write("You lose!",font=('Arial', 9, 'normal'))
    if end == "blocks":#when all blocks are destroyed
        writer.setpos([-47,-30])
        writer.write("You win!",font=('Arial', 9, 'normal'))
def setup():
    startvariance = 60 #determines the range that the bullets starting position can be in
    #put the various turtles in their proper positions 
    bullet.penup()
    bullet.speed(8)#8
    scorewriter.speed(0)
    scorewriter.penup()
    scorewriter.setpos(-280,-275)
    turtle.setup(600,600)
    mainblock.speed(0)
    mainblock.penup()
    mainblock.shape("square")
    mainblock.shapesize(1,4)
    mainblock.setpos(0,-250)
    bullet.setpos(0,-200)
    bullet.left(90)
    bullet.right(random.randrange(-startvariance,startvariance,step=1))
    bullet.pendown()
    #tells the turtle to listen to these keys
    turtle.listen()
    turtle.onkeypress(startright,"Right") #runs function startright on keypress right
    turtle.onkeypress(startleft,"Left") 
    turtle.onkeyrelease(endright,"Right")
    turtle.onkeyrelease(endleft,"Left")
    turtle.onkey(quit,"q")
#note: the reason why you can call the functions like startright even though they aren't defined until later lines is because the setup() function isnt ran until it's called later in the main module.
def setstartgame(x,y):#used to start game
    global gamestart
    global started
    started = True
    if gamestart != True:
        print("Starting Game...")
        turtle.hideturtle()
        gamestart = True
        placeblocks()
    else:
        print("Game already started")

def startgame():
    global gamestart
    global started
    if started != True:#prevents this from rerunning after the game has already started
        turtle.onscreenclick(setstartgame)#create onscreenclick event to start game
        turtle.speed(2)
        turtle.goto(-43,0)
        turtle.write("Start game?",font=('Arial', 9, 'normal'))
        turtle.goto(-45,0)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(90)
    #turtle.onscreenclick(setstartgame)
    if gamestart == True:
        turtle.clear()
    
    

    
def startright():#starts moving the block to the right
    global right 
    right = True
def startleft():#starts moving the block to the left
    global left
    left = True
def endright():#stops the block from moving right on keyrelease
    global right 
    right = False
def endleft():#stops the block from moving left on keyrelease
    global left
    left = False

def movright():#moves block right
    x = mainblock.xcor()
    y = mainblock.ycor()
    mainblock.setpos(x+5,y)#default 10
def movleft():#moves block left
    x = mainblock.xcor()
    y = mainblock.ycor()
    mainblock.setpos(x-5,y)#default 10
def bullettick():#moves the bullet slightly forward when called
    bullet.forward(5)#default 5
def calculatescore():#keeps track of score and adds to it when a block is hit. Score is multiplied with each block hit without touching the ball
    global score
    global lasthit
    global killcount
    lasthit += 1
    score += 10 * (lasthit)
    scorewriter.clear()
    scorewriter.write("Score: "+str(score)+"  Multiplier: "+str(lasthit+1)+"  Blocks Destroyed: "+str(killcount),font=('Arial', 9, 'normal'))
def blockdetection():
    global allblocks
    global killcount
    line = int()
    hitindex = int()
    hitindex = 20
    hit = str()
    if 145 < bullet.ycor() < 155: #detects if bullet is on first row
        line = 0
        if -270 < bullet.xcor() < -230:#detects if bullet is in the first column
            hitindex = 0
        elif -220 < bullet.xcor() < -180:
            hitindex = 1
        elif -170 < bullet.xcor() < -130:
            hitindex = 2
        elif -120 < bullet.xcor() < -80:
            hitindex = 3
        elif -70 < bullet.xcor() < -30:
            hitindex = 4
        elif -20 < bullet.xcor() < 20:
            hitindex = 5
        elif 30 < bullet.xcor() < 70:
            hitindex = 6
        elif 80 < bullet.xcor() < 120:
            hitindex = 7
        elif 130 < bullet.xcor() < 170:
            hitindex = 8
        elif 180 < bullet.xcor() < 220:
            hitindex = 9
        elif 230 < bullet.xcor() < 270:
            hitindex = 10
    if 170 < bullet.ycor() < 180:#detects if bullet is on the second row
        line = 1
        if -270 < bullet.xcor() < -230:
            hitindex = 0
        elif -220 < bullet.xcor() < -180:
            hitindex = 1
        elif -170 < bullet.xcor() < -130:
            hitindex = 2
        elif -120 < bullet.xcor() < -80:
            hitindex = 3
        elif -70 < bullet.xcor() < -30:
            hitindex = 4
        elif -20 < bullet.xcor() < 20:
            hitindex = 5
        elif 30 < bullet.xcor() < 70:
            hitindex = 6
        elif 80 < bullet.xcor() < 120:
            hitindex = 7
        elif 130 < bullet.xcor() < 170:
            hitindex = 8
        elif 180 < bullet.xcor() < 220:
            hitindex = 9
        elif 230 < bullet.xcor() < 270:
            hitindex = 10
    if 195 < bullet.ycor() < 205:#detects if bullet is on the third row
        line = 2
        if -270 < bullet.xcor() < -230:
            hitindex = 0
        elif -220 < bullet.xcor() < -180:
            hitindex = 1
        elif -170 < bullet.xcor() < -130:
            hitindex = 2
        elif -120 < bullet.xcor() < -80:
            hitindex = 3
        elif -70 < bullet.xcor() < -30:
            hitindex = 4
        elif -20 < bullet.xcor() < 20:
            hitindex = 5
        elif 30 < bullet.xcor() < 70:
            hitindex = 6
        elif 80 < bullet.xcor() < 120:
            hitindex = 7
        elif 130 < bullet.xcor() < 170:
            hitindex = 8
        elif 180 < bullet.xcor() < 220:
            hitindex = 9
        elif 230 < bullet.xcor() < 270:
            hitindex = 10
    if 220 < bullet.ycor() < 230:#detects if bullet is on the fourth row
        line = 3
        if -270 < bullet.xcor() < -230:
            hitindex = 0
        elif -220 < bullet.xcor() < -180:
            hitindex = 1
        elif -170 < bullet.xcor() < -130:
            hitindex = 2
        elif -120 < bullet.xcor() < -80:
            hitindex = 3
        elif -70 < bullet.xcor() < -30:
            hitindex = 4
        elif -20 < bullet.xcor() < 20:
            hitindex = 5
        elif 30 < bullet.xcor() < 70:
            hitindex = 6
        elif 80 < bullet.xcor() < 120:
            hitindex = 7
        elif 130 < bullet.xcor() < 170:
            hitindex = 8
        elif 180 < bullet.xcor() < 220:
            hitindex = 9
        elif 230 < bullet.xcor() < 270:
            hitindex = 10
    if 245 < bullet.ycor() < 255:#detects if bullet is on the fifth row
        line = 4
        if -270 < bullet.xcor() < -230:
            hitindex = 0
        elif -220 < bullet.xcor() < -180:
            hitindex = 1
        elif -170 < bullet.xcor() < -130:
            hitindex = 2
        elif -120 < bullet.xcor() < -80:
            hitindex = 3
        elif -70 < bullet.xcor() < -30:
            hitindex = 4
        elif -20 < bullet.xcor() < 20:
            hitindex = 5
        elif 30 < bullet.xcor() < 70:
            hitindex = 6
        elif 80 < bullet.xcor() < 120:
            hitindex = 7
        elif 130 < bullet.xcor() < 170:
            hitindex = 8
        elif 180 < bullet.xcor() < 220:
            hitindex = 9
        elif 230 < bullet.xcor() < 270:
            hitindex = 10
    if 270 < bullet.ycor() < 280:#detects if bullet is on the sixth row
        line = 5
        if -270 < bullet.xcor() < -230:
            hitindex = 0
        elif -220 < bullet.xcor() < -180:
            hitindex = 1
        elif -170 < bullet.xcor() < -130:
            hitindex = 2
        elif -120 < bullet.xcor() < -80:
            hitindex = 3
        elif -70 < bullet.xcor() < -30:
            hitindex = 4
        elif -20 < bullet.xcor() < 20:
            hitindex = 5
        elif 30 < bullet.xcor() < 70:
            hitindex = 6
        elif 80 < bullet.xcor() < 120:
            hitindex = 7
        elif 130 < bullet.xcor() < 170:
            hitindex = 8
        elif 180 < bullet.xcor() < 220:
            hitindex = 9
        elif 230 < bullet.xcor() < 270:
            hitindex = 10
    if hitindex == 20:
        hit = "miss"
        #print("Miss!")
    elif allblocks[line][hitindex].isvisible():
        allblocks[line][hitindex].hideturtle()
        hit = "hit"
        killcount += 1
        calculatescore()
        #print("Hit!")
    #detects side
    side = "none"
    if hit == "hit":#detects where block was hit from to determine the direction of the bounce
        xpo, ypo = allblocks[line][hitindex].pos()
        bxpo, bypo = bullet.pos()
        if ypo-5 < bypo < ypo-0:
            side = "bottom"
            bounce("ceiling")
        if ypo-0 < bypo < ypo+5:
            side = "top"
            bounce("topside")
        if xpo-20 < bxpo < xpo-15:
            side = "left"
            bounce("wallright")
        if xpo+15 < bxpo < xpo+20:
            side = "right"
            bounce("wallleft")
    #print(side)

            

def detection():#detects if the bullet hits the main block, wall, ceiling, or other blocks, and then sends the data to the bounce module
    #print(bullet.pos(),":",mainblock.pos()," rot:",bullet.heading()) #For debugging purposes
    global killcount
    if killcount >= 66:#keeps track of blocks killed and ends game when all are destroyed
        gameend("blocks")
    if (mainblock.ycor()+10)> bullet.ycor() > (mainblock.ycor()-10) and (mainblock.xcor()+40)> bullet.xcor() > (mainblock.xcor()-40):
        #print("hit!")
        bounce("mainblock")
        global lasthit
        lasthit = 0
        scorewriter.clear()
        scorewriter.write("Score: "+str(score)+"  Multiplier: "+str(lasthit+1)+"  Blocks Destroyed: "+str(killcount),font=('Arial', 9, 'normal'))
    elif bullet.xcor() > 290:
        #print("wallright!")
        bounce("wallright")
    elif bullet.xcor() < -295:
        #print("wallleft!")
        bounce("wallleft")
    elif bullet.ycor() > 300:
        #print("ceiling!")
        bounce("ceiling")
    elif bullet.ycor() < -300:
        #print("bottom!")
        gameend("offscreen")
    blockdetection()
def bounce(obj):#calculates new bullet trajectory based on where it hit.33
    rngrange = 5 #default 5. determines the the range of pixels that each bounce can be vary by
    newheading = int()
    if obj == "mainblock": #"bounces" the bullet off the main block
        if 180 < bullet.heading() < 270:
            newheading = 360 - bullet.heading()
            bullet.setheading(newheading)
        elif 270 <= bullet.heading() <= 360:
            newheading = 360 - bullet.heading()
            bullet.setheading(newheading)
        xpos, ypos = bullet.pos()
        bxpos, bypos = mainblock.pos()
        blockmod = (mainblock.xcor() - bullet.xcor())/2
        bullet.left(blockmod)
        if 180 < bullet.heading() < 270:
            bullet.setheading(175)
        elif 270 <= bullet.heading() <= 360:
            bullet.setheading(5)
        
        #print(blockmod) for debugging purposes
    if obj == "topside":#"bounces" the bullet off the topside
        if 180 < bullet.heading() < 270:
            newheading = 360 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
        elif 270 <= bullet.heading() <= 360:
            newheading = 360 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
    elif obj == "wallleft":
        if 180 > bullet.heading() > 90:
            newheading = 180 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
        elif bullet.heading() >= 180:
            newheading = 540 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
    elif obj == "wallright":
        if bullet.heading() <= 90:
            newheading = 180 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
        elif bullet.heading() >= 270:
            newheading = 540 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
    elif obj == "ceiling":
        if bullet.heading() <= 90:
            newheading = 360 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)
        elif 180 > bullet.heading() > 90:
            newheading = 360 - bullet.heading()
            newheading += random.randint(-rngrange, rngrange)
            bullet.setheading(newheading)



def maintick():#runs every 'tick'. responsible for running all the modules that need to be ran each second.
    bullettick()
    detection()
    if right == True:
        movright()
    if left == True:
        movleft()
def main():
    global gamestart
    previousint = 0
    setup()#calls the setup module
    while True:
        
        startgame()
        while gamestart == True: #these next few lines makes maintick() run every .2 seconds. without these lines or with a delay less than .2 the game changes speed when moving the mainblock.
            timeint = round(time.time(),2) #saves time up to two decimal places.
            if timeint > previousint+.01: #if lower than .02 the game slows down when moving the block.
                maintick()#calls the maintick() module
                previousint = timeint
            #print(timeint) #for debugging purposes
main()








