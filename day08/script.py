# task 1.1
# import pyjokes

# joke = pyjokes.get_joke("en", "neutral")
# print(joke)

# task 2.1

# import turtle
# my_turtle = turtle.Turtle()

# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.right(90)
# turtle.done()

# task 2.2

# import turtle
# toto = turtle.Screen()
# toto.bgcolor("black")
# titi = turtle.Turtle()
# titi.color( "red")
# for i in range(10):
#     titi.right(90 + (i * 2))
#     titi.circle(42 + (i * 1.3))
# toto.exitonclick()

# task 2.3

# import turtle

# nb_sides = int(input("number of sides : "))
# size = int(input("size : "))
# toto = turtle.Screen()
# toto.bgcolor("black")
# titi = turtle.Turtle()
# titi.color("red")

# for i in range(nb_sides):
#     titi.forward(size)
#     titi.right(360/nb_sides)
# toto.exitonclick()

# task 2.4

# import turtle as t

# t.speed = 0
# t.tracer(100,1)
# t.penup()
# t.goto(0, -350)
# t.pendown()

# for i in reversed(range(360)):
#     t.circle(i,20)

# t.exitonclick()

# task 3.1

import pygame as pygame

