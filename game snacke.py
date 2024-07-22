from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s = Screen()
s.setup(height=600,width=600)
s.bgcolor("black")
s.title("Snacke Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    #Detect food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    #Detect wall
    if snake.head.xcor() > 282 or snake.head.ycor() > 280 or snake.head.ycor()<-280 or snake.head.xcor()<-282:
        is_game_on = False
        score.game_over()
    
    #Detect tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

s.exitonclick()
