from turtle import Screen, Turtle
import time
from snake import Snake


screen = Screen()
screen.title("My snake game")
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
snake = Snake()
game_is_on = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()