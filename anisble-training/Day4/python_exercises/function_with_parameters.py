#!/usr/bin/pyth

def F1():
 print("F1() with zero arguments") 

def F1(x):
 print(type(x))
 x="hello"
 print(type(x))
 x=20000000000000000000000000000000000000000000000000000000000000000000000
 print(type(x))
F1(100)
