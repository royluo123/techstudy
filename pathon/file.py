#! /usr/bin/python  
spath="E:/pathon/test.txt"  
f=open(spath,"w") # Opens file for writing.Creates this file doesn't exist.  
f.write("First line 1.\n")  
f.writelines("First line 2.")  
f.close()  
f=open(spath,"r") # Opens file for reading  
for line in f:  
  print("每一行的数据是:%s"%line)  
f.close()  
