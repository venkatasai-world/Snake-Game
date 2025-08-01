import time
from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard


screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # snake.move()

    # detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detact collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        # score.game_over()
        score.game_over()

    # detect collison with tail
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)< 13:
            game_is_on = False
            score.game_over()

    snake.move()


















screen.exitonclick()