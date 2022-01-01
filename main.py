import turtle

import pygame


obj=turtle.Turtle()


obj.speed(1)
obj.penup()
obj.goto(-100,200)
obj.pendown()
obj.begin_fill()
obj.fillcolor("red")
obj.forward(300)
obj.setheading(270)
obj.forward(180)
obj.setheading(180)
obj.forward(300)
obj.setheading(90)
obj.forward(180)
obj.end_fill()


# obj.penup()
# obj.setpos(0,130)
# obj.pendown()
# obj.fillcolor("yellow")
# obj.begin_fill()
# for i in range(5):
#     obj.forward(100)
#     obj.right(144)
# obj.end_fill()

obj.penup()
obj.setpos(30,120)
obj.pendown()
angle = 140
obj.fillcolor("yellow")
obj.begin_fill()
for side in range(5):
    obj.forward(35)
    obj.right(angle)
    obj.forward(35)
    obj.right(72 - angle)
obj.end_fill()




obj.color('black')

obj.setheading(180)
obj.penup()
obj.forward(130)
obj.pendown()

obj.begin_fill()
obj.fillcolor('gray')



obj.setheading(90)
obj.forward(130)


obj.setheading(180)
obj.forward(25)
obj.setheading(270)
obj.forward(450)

obj.setheading(180)
obj.forward(60)

obj.setheading(270)
obj.forward(30)
obj.setheading(360)
obj.forward(150)

obj.setheading(90)
obj.forward(30)

obj.setheading(180)
obj.forward(65)
obj.setheading(90)
obj.forward(450)
obj.end_fill()

obj.hideturtle()

turtle.done()