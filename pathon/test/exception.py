#!/usr/bin/python
# Filename: try_except.py
import sys
import time


try:
 s = input('Enter something --> ')
except EOFError:
 print ('\nWhy did you do an EOF on me?')
 sys.exit() # exit the program
except:
 print ('\nSome error/exception occurred.')
# here, we are not exiting the program
print ('Done')



try:
 f = open('test.txt')
 while True: # our usual file-reading idiom
  line = f.readline()
  if len(line) == 0:
   break
  time.sleep(2)
  print (line,)
finally:
 f.close()
 print ('Cleaning up...closed the file')
