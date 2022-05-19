import turtle

show = turtle.Turtle()
show.speed(100)
turtle.bgcolor("black")

if __name__ == "__main__":
    for i in range(250):
        show.color('cyan')
        show.circle(i)
        show.left(5)
    
    turtle.done()