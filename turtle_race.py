from turtle import Turtle
from turtle import Screen
import random

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
all_turtles = []    
y_position = -70
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
print(f"The winning turtle is the {winning_color} turtle!")
if winning_color == user_bet:
    print("You win!")
else:
    print("You lose!")

screen.title("Turtle race")
screen.exitonclick()
