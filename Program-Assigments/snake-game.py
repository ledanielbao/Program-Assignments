# DANIEL LE

# import requred modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# creating a window screen
screen = turtle.Screen()
screen.title("Daniel's Snake Game") 
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.traver(0)

# snake head
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "Stop"

# snake body
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
    # write score???

# food
food = turtle.Turtle()
colors = random.choice (['red', 'yellow', 'green', 'blue', 'pink'])
shapes = random.choice (['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(6,9)
    # x,y coordinates??

# key directions
def goup():
    if head.direction != "down":
        head.direction = "up"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        # finish def move() ??
    if head.direction == "left":
        x = head.xcor() 
        # dont know if this is right lol
    if head.direction == "down":
        y = head.ycor()
    if head.direction == "right":
        x = head.xcor()
        # dont know if this is right lol

screen.listen()
screen.onkeypress(goup, "w")
screen.onkeypress(goleft, "a")
screen.onkeypress(godown, "s")
screen.onkeypress(goright, "d")