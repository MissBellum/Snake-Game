from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor('black')
screen.title('Snake Xenia')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.up_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        game_on = False
        score.game_over()
    for each in snake.piece[1:]:
        if snake.head.distance(each) < 18:
            game_on = False
            score.game_over()

screen.exitonclick()