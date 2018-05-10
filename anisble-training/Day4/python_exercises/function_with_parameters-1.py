#!/usr/bin/pyth

def F1():
 print("F1() with zero arguments") 

def F2(x):
 print ("F2() with one arguments") 
 print(type(x))
 x="hello"
 print(type(x))
 x=20000000000000000000000000000000000000000000000000000000000000000000000
 print(type(x))

F2(100)

F1()
