#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:56:23 2019

@author: jlopes

Based in: John DeNero. Composing Programs, "1.6.5 Example: Newton's Method",
https://composingprograms.com/pages/16-higher-order-functions.html

Based in: Harold Abelson and Gerald Jay Sussman,
Structure and Interpretation of Computer Programs
"""


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
    def f(x):
        return x * x - a

    def df(x):
        return 2 * x

    return find_zero(f, df)


# tests
print(square_root_newton(64))
print(square_root_newton(81))
