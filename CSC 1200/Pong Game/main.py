'''
Date : 4/12/2023

Name : Austin Ring, David Miller, John Taylor

Class : CSC 1200

Assignment : Group Project - Pong

Problem: Creating the classic game, Pong in Python
'''
import turtle
 
# Screen
sc = turtle.Screen()
sc.title("Pong")
sc.bgcolor("black")
sc.setup(width=1000, height=600)
  
# Left paddle
left = turtle.Turtle()
left.shape("square")
left.color("green")
left.shapesize(stretch_wid=6, stretch_len=2)
left.penup()
left.goto(-400, 0)
  
# Right paddle
right = turtle.Turtle()
right.shape("square")
right.color("green")
right.shapesize(stretch_wid=6, stretch_len=2)
right.penup()
right.goto(400, 0)
  
# creates the ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("red")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5
  
# Initialize the score
playerOne = 0
playerTwo = 0
  
# Scoreboard
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player One : 0    Player Two: 0", align="center", font=("Copperplate", 24, "normal"))
 
 
# functions that let the paddles move up and down
def paddleaup():
    y = left.ycor()
    y += 20
    left.sety(y)
  
def paddleadown():
    y = left.ycor()
    y -= 20
    left.sety(y)
 
def paddlebup():
    y = right.ycor()
    y += 20
    right.sety(y)
  
def paddlebdown():
    y = right.ycor()
    y -= 20
    right.sety(y)
 
sc.listen()
#Player 1 controls
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
#Player 2 controles
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")
 
while (playerOne < 10 and playerTwo < 10):
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
 
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
 
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
 
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        playerOne += 1
        sketch.clear()
        sketch.write("Player One : {}   Player Two: {}".format(playerOne, playerTwo), align="center", font=("Copperplate", 24, "normal"))
 
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        playerTwo += 1
        sketch.clear()
        sketch.write("Player One : {}   Player Two: {}".format(playerOne, playerTwo), align="center", font=("Copperplate", 24, "normal"))
 
    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right.ycor()+75 and hit_ball.ycor() > right.ycor()-75):
        hit_ball.setx(360)
        hit_ball.dx*=-1
        
    if (hit_ball.xcor()<-360 and hit_ball.xcor()>-370) and (hit_ball.ycor()<left.ycor()+75 and hit_ball.ycor()>left.ycor()-75):
        hit_ball.setx(-360)
        hit_ball.dx*=-1