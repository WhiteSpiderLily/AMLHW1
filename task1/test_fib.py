# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:25:10 2019

@author: Siyuan
"""

def fib(x):
    a1, a2 = 1, 1
    if x <= 2:
        return a2
    else:
        for i in range(2, x):
            a2 = a1 + a2
            a1 = a2 - a1
        return a2


def test_answer():
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(12) == 144
