import turtle
import time
import random
delay = 0.1
#SCORE
score=0
high_score = 0

wn = turtle.Screen() #Setting up the Screen
wn.title("SNAKE GAME USING PYTHON")
wn.bgcolor("Green")
wn.setup(width = 600, height = 600)
wn.tracer(0) #Turns off the screen updates
#Setting up of snake head
head= turtle.Turtle()
head.speed(0) #animation Speed
head.shape("square")
head.color("orange")
head.penup()
head.goto(0,0)
head.direction= "stop"

#Setting up of snake Food
food= turtle.Turtle()
food.speed(0) #animation Speed
food.shape("circle")
food.color("blue")
food.penup()
head.goto(0,100)
segments = []
# Pen Set up
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 \tHigh Score: 0", align="center", font =("Courier",24,"normal"))
#Defining Of Functions
def go_up():
    if head.direction != "down":
     head.direction ="up"
def go_down():
    if head.direction != "up":
     head.direction ="down"
def go_right():
    if head.direction != "left":
     head.direction ="right"
def go_left():
    if head.direction != "right":
     head.direction ="left"     
           
def move():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y+20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y-20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x+20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x-20)
 
wn.listen()
wn.onkeypress(go_up, "w")    
wn.onkeypress(go_down, "s")   
wn.onkeypress(go_right, "d")   
wn.onkeypress(go_left, "a")   
 
# Main Game Loop
while True:
    wn.update()
    #COLLIDING WITH BORDERS
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # HIDING THE SEGMENTS
        for segment in segments:
            segment.goto(1000,1000)
        # Clearing off the segments
        segments.clear()
        # Reset of Score
        score = 0
        #RESET THE DELAY
        delay=0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        
        new_segment= turtle.Turtle()
        new_segment.speed(0) #animation Speed
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        #SHORTENING THE DELAY
        delay-=0.001
        #INCREASING SCORE BY 10
        score += 10
        
        if score > high_score:
            high_score=score
            
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score))

    for index in range(len(segments)-1,0,-1):  
        x = segments[index-1].xcor() 
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    if len(segments) > 0:
        x=head.xcor()   
        y=head.ycor() 
        segments[0].goto(x,y)  
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # Hide the Segment
            for segment in segments:
              segment.goto(1000,1000)
             # Clearing off the segments
            segments.clear()
            
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
wn.mainloop()
