import turtle
import math

flower = turtle.Turtle()
flower.color("red", "yellow")
flower.speed(50)
flower.getscreen().bgcolor("black")

if __name__ == "__main__":
    flower.begin_fill()
    for i in range(52):
            flower.forward(450)
            flower.left(170)
    flower.end_fill()
    turtle.done()

