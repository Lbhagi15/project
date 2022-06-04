import turtle

bhagi=turtle.Turtle()
bhagi.getscreen().bgcolor("black")
bhagi.penup()
bhagi.goto(-200,100)
bhagi.pendown()
bhagi.color("cyan","orange",)
bhagi.speed(20)
def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle,size/3)
            turtle.left(216)
            turtle.end_fill()
star(bhagi,360)
turtle.done()