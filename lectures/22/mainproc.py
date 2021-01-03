# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:43:50 2018

@author: jlopes
"""

import turtle


def drawSquare(t, sz):
    """
    Make turtle t draw a square of with side sz.
    """
    for i in range(4):
        t.forward(sz)
        t.left(90)

# 1. without using main()
#wn = turtle.Screen()          # Set up the window and its attributes
#wn.bgcolor("lightgreen")
#
#alex = turtle.Turtle()        # Create alex
#drawSquare(alex, 50)          # Call the function to draw the square
#
#wn.mainloop()
#turtle.bye()

# 2. using main()
#def main():                     # Define the main function
#    wn = turtle.Screen()        # Set up the window and its attributes
#    wn.bgcolor("lightgreen")
#
#    alex = turtle.Turtle()      # Create alex
#    drawSquare(alex, 50)        # Call the function to draw the square
#
#    wn.exitonclick()
#    turtle.bye()
#
#main()                          # Invoke the main function
