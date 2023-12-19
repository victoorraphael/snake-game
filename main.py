from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

s = Snake()
f = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    s.move()

    # Detect collision with food
    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        scoreboard.add_point()

    # Detect collision with walls
    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        game_running = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in s.segments[1:]:
        if s.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()


screen.exitonclick()
