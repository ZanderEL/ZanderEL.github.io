# Import turtle
from turtle import *


# Set the stumpsize variable
stumpsize = 100


# Set the grassheight variable
grassheight = 225


# Set the background color
bgcolor("lightblue")


# Set the speed of drawing
speed(5)


# Create grass by changing pen color to green, going to the bottom, and drawing green across the screen
penup()
pencolor("green")
goto(-400,-225)
pensize(grassheight)
pendown()
forward(1000)
penup()


# Create sun by going to top right and changing pen color to yellow
goto(300,250)
pencolor("yellow")
pendown()
forward(1)
penup()


# Draw the stump of the tree and fill in the stump
goto(-100,-150)
pensize(1)
pendown()
left(180)
pencolor("brown")
fillcolor("brown")
begin_fill()
for i in range(4):
    forward(stumpsize)
    right(90)
end_fill()
right(180)
penup()


# Check if the drawing speed is less than 10 and if so set the drawing speed to 10
if speed() < 10:
    speed(10)


# Draw the leaves of the tree
goto(-250,-50)
pencolor("green")
pendown()
fillcolor("green")
begin_fill()
for i in range(3):
    forward(200)
    left(120)
end_fill()


# End code and keep window open
done()