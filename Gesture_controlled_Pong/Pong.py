import turtle
import winsound

# creating the window using turtle

window = turtle.Screen()
window.bgcolor("Blue")
window.setup(height=600, width=800)
window.tracer(0)

# variables
A_score = 0
B_score = 0

# Creating Objects

# Paddle A
'''This is a turtle object u can do any stuff with it'''
paddle_A = turtle.Turtle()
paddle_A.shape("square")
'''this is animation speed of the obj'''
paddle_A.speed(0)
paddle_A.color('white')
'''This makes sure that if the obj is moved it doesn't draw a line '''
paddle_A.penup()
'''This is used to reshape the turtle obj'''
paddle_A.shapesize(stretch_len=1, stretch_wid=5)

'''In turtle, the coordinates have origin at centre'''
paddle_A.goto(-350, 0)


# Paddle B
'''This is a turtle object u can do any stuff with it'''
paddle_B = turtle.Turtle()
'''this is animation speed of the obj'''
paddle_A.speed(0)

paddle_B.shape("square")
paddle_B.color('white')
'''This makes sure that if the obj is moved it doesn't draw a line '''
paddle_B.penup()
'''This is used to reshape the turtle obj'''
paddle_B.shapesize(stretch_len=1, stretch_wid=5)
'''In turtle, the coordinates have origin at centre'''
paddle_B.goto(350, 0)

# Ball
'''This is a turtle object u can do any stuff with it'''
ball = turtle.Turtle()
ball.shape("square")
'''this is animation speed of the obj'''
paddle_A.speed(0)

ball.color('white')
'''This makes sure that if the obj is moved it doesn't draw a line '''
ball.penup()
'''In turtle, the coordinates have origin at centre'''
ball.goto(0, 0)
# Setting the ball movement speed GOTO line 83 for implementation
ball.dx = 0.1
ball.dy = -0.1

# Text
Text = turtle.Turtle()
'''this is animation speed of the obj'''
Text.speed(0)
Text.color("white")
'''This makes sure that if the obj is moved it doesn't draw a line '''
Text.penup()
Text.hideturtle()
Text.sety(260)

# FUNCTIONS


def paddle_A_UP():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y=y)


def paddle_A_Down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y=y)


def paddle_B_UP():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y=y)


def paddle_B_Down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y=y)

# Keyboard binding


# window.listen()
# window.onkeypress(paddle_A_UP, 'w')
# window.onkeypress(paddle_A_Down, 's')
# window.onkeypress(paddle_B_UP, 'Up')
# window.onkeypress(paddle_B_Down, 'Down')



# Main game loop
while True:
    # This shit updates the screen everytime the loop is runned
    window.update()

    # This is the way to move the ball!
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        winsound.PlaySound("Recording.m4a",winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        winsound.PlaySound("Recording.m4a",winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *= -1
    # SCORE MANAGEMENT!
    if ball.xcor() > 390:
        A_score += 1
        Text.clear()
        Text.write(f"Player A :  {A_score}   |    Player B :   {B_score}",
                   align='center', font=('Orbitron', 24, 'normal'))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        B_score += 1
        Text.clear()
        Text.write(f"Player A :  {A_score}   |    Player B :   {B_score}",
                   align='center', font=('Orbitron', 24, 'normal'))
        ball.goto(0, 0)
        ball.dx *= -1
    # BALL AND PALLET COLLISION
    # Paddle B
    if (340 < ball.xcor() < 350) and (paddle_B.ycor() - 40 < ball.ycor() < paddle_B.ycor() + 40):
        winsound.PlaySound("Recording.m4a",winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1
    # Paddle A
    if (-340 > ball.xcor() > -350) and (paddle_A.ycor() - 40 < ball.ycor() < paddle_A.ycor() + 50):
        winsound.PlaySound("Recording.m4a",winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
