import turtle

turtle.speed(10)
turtle.bgcolor("black")

for x in range(5):
    for colours in ["red", "cyan", "lime", "lightblue", "magenta", "orange"]:
        turtle.color(colours)
        turtle.pensize(3)
        turtle.lt(12)
        for x in range(4):
            turtle.fd(200)
            turtle.lt(90)

turtle.done()
