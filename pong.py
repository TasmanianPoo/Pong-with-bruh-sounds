import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by pee")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2


#scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align= "center", font=("Courier", 24, "normal"))

score_a = 0
score_b = 0

#Function paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 30
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 30
    paddle_a.sety(y)

def paddle_a_right():
    x = paddle_a. xcor()
    if x < -200:
        x += 30
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a. xcor()
    if x > -380:
        x -= 30
    paddle_a.setx(x)



#paddle b function
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 30
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 30
    paddle_b.sety(y)

def paddle_b_right():
    x = paddle_b. xcor()
    if x > 200:
        x -= 30
    paddle_b.setx(x)

def paddle_b_left():
    x = paddle_b. xcor()
    if x < 380:
        x += 30
    paddle_b.setx(x)

#controls
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_right, "Left")
wn.onkeypress(paddle_b_left, "Right")
wn.onkeypress(paddle_b_down, "Down")


#collision detection
def check_collision(ball, paddle):
    if (paddle.ycor()-50 <ball.ycor()< paddle.ycor()+50):
        if (paddle.xcor() -10 < ball.xcor()< paddle.xcor()+10):
            return True
    return False


# game loop

while True:
    wn.update()

    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Comic Sans MS", 24, "normal"))
        winsound.PlaySound("gotem.wav.wav", winsound.SND_ASYNC)


    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))
        winsound.PlaySound("gotem.wav.wav", winsound.SND_ASYNC)


    #paddle ball collision

    if(ball.dx < 0) and check_collision(ball,paddle_a):
        ball.setx(paddle_a.xcor() +10)
        ball.dx *= -1
        winsound.PlaySound("bruh.wav.wav", winsound.SND_ASYNC)

    if (ball.dx > 0) and check_collision(ball, paddle_b):
        ball.setx(paddle_b.xcor() -10)
        ball.dx *= -1
        winsound.PlaySound("bruh.wav.wav", winsound.SND_ASYNC)








