import sys
import time
#from shutil import move
from turtle import Screen, Turtle

from scoreboard import ScoreBoard, ALIGNMENT, FONT
from snake import Snake
from food import Food

def stop_game():
    global game_is_on
    game_is_on = False
    snake.beyond_screen()
    food.color("black")
    stop = Turtle()
    stop.hideturtle()
    stop.color("white")
    stop.write("GAME OVER.",align=ALIGNMENT, font=FONT)
    screen.update()
    time.sleep(3)
    sys.exit()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# food = Turtle("circle")
# food.shapesize(0.5,0.5)
# food.color("red")

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "q")
# segments = []
#
# starting_position = [(0, 0),(-20, 0), (-30, 0)]
# for position in starting_position:
    # new_segment = Turtle(shape="square")
    # new_segment.color("white")
    # new_segment.penup()
    # new_segment.goto(position)
    # segments.append(new_segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.4)
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) <20 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # for seg_num in range(len(segments) - 1, 0 , -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    #
    # segments[0].forward(20)
    # segments[0].left(30)
    if snake.head.xcor() >300  or snake.head.xcor() <-300 or  snake.head.ycor() >300 or snake.head.ycor() < -300:
        #game_is_on = False
        snake.reset()
        scoreboard.reset()


#Detect collision head with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
             scoreboard.reset()
             snake.reset()



screen.exitonclick()
