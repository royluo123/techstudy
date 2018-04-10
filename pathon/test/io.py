#!/usr/bin/python
# Filename: using_file.py

import pickle as p
#import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object
shoplist = ['apple', 'mango', 'carrot']
# Write to the file
f = open(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
f.close()
del shoplist # remove the shoplist
# Read back from the storage
f = open(shoplistfile)
storedlist = p.load(f)
print (storedlist)



poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
# open for 'w'riting
f = open('test.txt', 'w')
f.write(poem) # write text to file
f.close() # close the file
f = open('test.txt')
# if no mode is specified, 'r'ead mode is assumed by default
while True:
 line = f.readline()
 if len(line) == 0: # Zero length indicates EOF
  break
 print (line,)
# Notice comma to avoid automatic newline added by Python
f.close() # close the file
