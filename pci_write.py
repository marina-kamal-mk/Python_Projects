# Program to draw rectangle in Python Turtle
import turtle
from turtle import *
import time



s=turtle.Turtle()
#time.sleep(10)
s.penup()
s.goto(0,270)
s.pendown()
style=('courier',20,'bold')
s.write('PCI Bus Write operation',align='center',font=style)
x=0
s.speed(10)
s.penup()
s.goto(-335,200)
s.pendown()
s.color('green')
style=('courier',10)
s.write('Clk',align='right',font=style)
#s.setpos(-370,200)
#clock
s.forward(30)
s.left(90)
while x<6:
    s.forward(50)
    s.right(90)
    s.forward(50)
    s.right(90)
    s.forward(50)
    s.left(90)
    s.forward(50)
    s.left(90)
    x=x+1

s.right(90)

s.penup()
s.goto(-335,170)
s.pendown()


s.speed(8)
#frame
s.color('blue')
style=('courier',10)
s.write('FRAME#', align='right',font=style)

s.forward(80)
s.right(90)
s.forward(50)
s.left(90)
s.forward(300)
s.left(90)
s.forward(50)
s.right(90)
s.forward(250)

#AD
s.penup()
s.goto(-335,97)
s.pendown()

s.color('DarkRed')
style=('courier',10)
s.write('AD', align='right',font=style)

s.forward(80)
s.left(90)
r=0
for i in range(0,4):
    s.color('DarkRed')
    #rectangle
    s.forward(10)
    s.right(90)
    s.forward(100)
    s.right(90)
    s.forward(20)
    s.right(90)
    s.forward(100)
    s.right(90)
    s.forward(10)
    s.right(90)

    s.penup()
    s.goto(-155+r,97)
    s.pendown()
    s.left(90)

    if i==0:
        s.penup()
        s.goto(-168+r,90)
        s.color('Crimson')
        style = ('courier', 10)
        s.write('address',align='right',font=style)
        s.goto(-155 + r, 97)
        s.pendown()
    else:
        s.penup()
        s.goto(-168 + r, 90)
        s.color('Crimson')
        style = ('courier', 10)
        s.write('data', align='right', font=style)
        s.goto(-155 + r, 97)
        s.pendown()
    r = r + 100

s.color('DarkRed')
s.right(90)
s.forward(150)

#c/be
s.penup()
s.goto(-335,55)
s.pendown()

s.color('DarkRed')
style=('courier',10)
s.write('C/BE#', align='right',font=style)

s.forward(80)
s.left(90)
r=0
for i in range(0,4):
    s.color('DarkRed')
    #rectangle
    s.forward(10)
    s.right(90)
    s.forward(100)
    s.right(90)
    s.forward(20)
    s.right(90)
    s.forward(100)
    s.right(90)
    s.forward(10)
    s.right(90)

    s.penup()
    s.goto(-155+r,55)
    s.pendown()
    s.left(90)

    if i==0:
        s.penup()
        s.goto(-168+r,47)
        s.color('Crimson')
        style = ('courier', 10)
        s.write('Command',align='right',font=style)
        s.goto(-155 + r, 55)
        s.pendown()
    else:
        s.penup()
        s.goto(-168 + r, 47)
        s.color('Crimson')
        style = ('courier', 10)
        s.write('BE', align='right', font=style)
        s.goto(-155 + r, 55)
        s.pendown()
    r=r+100

s.color('DarkRed')
s.right(90)
s.forward(150)


#irdy,trdy,devsel
s.penup()
s.goto(-335,-30)
s.pendown()


s.color('Teal')
style=('courier',10)
s.write('IRDY#', align='right',font=style)


s.forward(180)
s.right(90)
s.forward(50)
s.left(90)
s.forward(300)
s.left(90)
s.forward(50)
s.right(90)
s.forward(150)

s.penup()
s.goto(-335,-100)
s.pendown()


s.color('Indigo')
style=('courier',10)
s.write('TRDY#', align='right',font=style)


s.forward(180)
s.right(90)
s.forward(50)
s.left(90)
s.forward(300)
s.left(90)
s.forward(50)
s.right(90)
s.forward(150)

s.penup()
s.goto(-335,-170)
s.pendown()


s.color('Indigo')
style=('courier',10)
s.write('Dsel#', align='right',font=style)

s.forward(180)
s.right(90)
s.forward(50)
s.left(90)
s.forward(300)
s.left(90)
s.forward(50)
s.right(90)
s.forward(150)


done()

