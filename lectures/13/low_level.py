# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:05:58 2018

@author: jlopes

Peter Wentworth, Jeffrey Elkner, Allen B. Downey, and Chris Meyers,
How to Think Like a Computer Scientist — Learning with Python 3, 2012
"""


def koch_0(pen, size):
    pen.forward(size)


def koch_1(pen, size):
    for angle in [60, -120, 60, 0]:
        koch_0(pen, size/3)
        pen.left(angle)


def koch_2(pen, size):
    for angle in [60, -120, 60, 0]:
        koch_1(pen, size/3)
        pen.left(angle)


def koch_3(pen, size):
    for angle in [60, -120, 60, 0]:
        koch_2(pen, size/3)
        pen.left(angle)


# get a pen
import turtle

canvas = turtle.Screen()
canvas.setup(800, 300)
canvas.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pencolor("blue")
tess.shape("circle")
tess.shapesize(0.1)

tess.penup()
tess.goto(-300, -100)
tess.pendown()

#koch_0(tess, 600)
#koch_1(tess, 600)
#koch_2(tess, 600)
koch_3(tess, 600)

canvas.mainloop()     # Wait for user to close window
turtle.bye()
