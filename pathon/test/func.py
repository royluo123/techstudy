#!/usr/bin/python
# Filename: func_param.py
def printMax(a, b):
 if a > b:
  print (a, 'is maximum')
 else:
  print (b, 'is maximum')
printMax(3, 4) # directly give literal values
x = 5
y = 7
printMax(x, y) # give variables as arguments


#local/global variabe
def func(x):
 global y
 print ('x is', x)
 x = 2
 y = 4
 print ('Changed local x to', x)

x = 50
y=30
func(x)
print ('x is still', x) 
print ('y is change', y)


#default param
def say(message, times = 1):
 print (message * times)
say('Hello')
say('World', 5) 


#key param
def keyfunc(a, b=5, c=10):
 print ('a is', a, 'and b is', b, 'and c is', c)
keyfunc(3, 7)
keyfunc(25, c=24)
keyfunc(c=50, a=10)


#return
def maximum(x, y):
 if x > y:
  return x
 else:
  return y
print (maximum(2, 3))


#DocString
def printMax(x, y):
 '''Prints the maximum of two numbers.
 The two values must be integers.'''
 x = int(x) # convert to integers, if possible
 y = int(y)
 if x > y:
  print (x, 'is maximum')
 else:
  print (y, 'is maximum')
printMax(3, 5)
print (printMax.__doc__)
