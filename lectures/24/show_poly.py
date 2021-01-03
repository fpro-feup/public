# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:46:51 2018

@author: jlopes
"""

import turtle
import time


def show_poly():
    try:
        win = turtle.Screen()  # Grab/create a resource (e.g. a window)
        win.setup(800, 600),
        win.bgcolor("lightgreen")
        tess = turtle.Turtle()
        
        # This dialog could be cancelled,
        #   or the conversion to int might fail, 
        #   or n might be zero.
        n = int(input("How many sides do you want in your polygon? "))
        angle = 360 / n
        for i in range(n):     # Draw the polygon
            tess.forward(20)
            tess.left(angle)
        time.sleep(5)          # Make program wait a few seconds
    finally:
        win.bye()              # Release the resource (close the window)


show_poly()
