from turtle import Turtle, Screen
import random


def starting_position(turtle_name, x, y):
    turtle_name.penup()
    turtle_name.goto(x=x, y=y)


def move_turtle(turtle_name):
    amount = random.randint(0, 10)
    turtle_name.forward(amount)


is_race_on = False
colors = ["red", "green", "yellow", "orange", "blue", "purple"]
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)

x = -220
y = -100
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    starting_position(tim, x, y)
    all_turtles.append(tim)
    y += 40

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        move_turtle(turtle)

screen.exitonclick()
