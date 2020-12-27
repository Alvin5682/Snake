import turtle
import time
import random
from library import *
def goup():
    if head.direction!="down":
        head.direction="up"
def godown():
    if head.direction!="up":
        head.direction="down"
def goleft():
    if head.direction!="right":
        head.direction="left"
def goright():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
delay=0.1
screen=turtle.getscreen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.direction="stop"
head.penup()
head.goto(0,100)

screen.listen()
screen.onkey(goup,"w")
screen.onkey(godown,"s")
screen.onkey(goleft,"a")
screen.onkey(goright,"d")

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.shapesize(0.5,0.5)
food.goto(0,0)

length=[]
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
score=0
h = open ("highscore.txt", "r").readlines()[(0)]
(highscore)=(h)
pen.clear()
pen.write(f"Score:{score} High score: {highscore}",align="center",font=("Courier", 24, "normal")
)

while True:
    screen.update()
    move()
    time.sleep(delay)
    if head.xcor()>=275 or head.ycor()<=-295 or head.xcor()<=-275 or head.ycor()>=295:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for item in length:
            item.goto(100000,100000)
        length=[]
        score=0
        pen.clear()
        pen.write(f"Score:{score} High score: {highscore}",align="center",font=("Courier", 24, "normal")
)
    for item in length:
        if item.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for item in length:
                item.goto(100000,100000)
            length=[]
            score=0
            pen.clear()
            pen.write(f"Score:{score} High score: {highscore}",align="center",font=("Courier", 24, "normal"))
    if head.distance(food)<15:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        newturtle=turtle.Turtle()
        newturtle.speed(0)
        newturtle.shape("square")
        newturtle.color("grey")
        newturtle.penup()
        length.append(newturtle)
        score=score+10
        if score>int(highscore):
            highscore=score
            f=open("highscore.txt","w")
            f.write(str(highscore))
            f.close()
        pen.clear()
        pen.write(f"Score:{score} High score: {highscore}",align="center",font=("Courier", 24, "normal")
)
    for i in range(len(length)-1,0,-1):
        x=length[i-1].xcor()
        y=length[i-1].ycor()
        length[i].goto(x,y)
    if len(length)>0:
        x=head.xcor()
        y=head.ycor()
        length[0].goto(x,y)
screen.exitonclick()