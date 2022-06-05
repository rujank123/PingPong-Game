import turtle
wn = turtle.Screen()
wn.title("Rujan")
wn.bgcolor("black") 
wn.setup(width=800, height=600 )
wn.tracer(0)  #turns turtle animation on/off and set delay for update drawing

#score
score_a = 0
score_b = 0

#Side A
side_a = turtle.Turtle()
side_a.speed(0)
side_a.shape("square")
side_a.shapesize(stretch_wid=5, stretch_len=1)
side_a.color("gold")
side_a.penup()
side_a.goto(-350, 0)

#Side B
side_b = turtle.Turtle()
side_b.speed(0)
side_b.shape("square")
side_b.shapesize(stretch_wid=5, stretch_len=1)
side_b.color("gold")
side_b.penup()
side_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("gold")
pen.penup()
pen.hideturtle() #make the turtle invisible
pen.goto(0, 260)
# pen.fillcolor("red")
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold") )

#Function
def side_a_up():
    y = side_a.ycor()
    y += 20
    side_a.sety(y)

def side_a_down():
    y = side_a.ycor()
    y -= 20
    side_a.sety(y) #sety=>positing along the y-axis (vertically)

def side_b_up():
    y = side_b.ycor()  #ycor=>Return the turtle's y cordinate
    y += 20
    side_b.sety(y)

def side_b_down():
    y = side_b.ycor()
    y -= 20
    side_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(side_a_up, "w")    
wn.onkeypress(side_a_down, "s")  
wn.onkeypress(side_b_up, "Up")    
wn.onkeypress(side_b_down, "Down")

#Main game loop
while True:
    wn.update()


    #Move the ball 
    ball.setx(ball.xcor() + ball.dx) #setx=>set the turtle first cordinate to x and second coordinate unchanged
                                    # xcor=>return the turtle x coordinate
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1   
        score_a += 1 
        pen.clear() #clear=>Delete the turtle drawing from the screen and dont move the turtle
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold" ) )

         

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1 
        score_b += 1 
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold" ) )

            

    #side and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < side_b.ycor() + 50 and ball.ycor() > side_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1   
        

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < side_a.ycor() + 50 and ball.ycor() > side_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1    
   