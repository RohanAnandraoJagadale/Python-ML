import turtle
turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(10)

colors = ["white","red", "yellow","cyan","magenta","green"]
for i in range(6):
    for color1 in colors:
        turtle.color(color1)
        turtle.circle(100)
        turtle.left(10)

turtle.hide()
turtle.done()