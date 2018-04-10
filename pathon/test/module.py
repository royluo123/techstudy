#!/usr/bin/python
# Filename: module.py
import sys
import func

#sys
print ('The command line arguments are:')
for i in sys.argv:
 print (i)
print ('\n\nThe PYTHONPATH is', sys.path, '\n') 


#name
if __name__ == '__main__':
 print ('This program is being run by itself')
else:
 print ('I am being imported from another module')


#func
func.say('World', 5)


#dir
dir(func)
dir(sys)
