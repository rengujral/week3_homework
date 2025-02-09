#!/usr/bin/python
from itertools import count
from traceback import print_tb
from xml.dom.minidom import ProcessingInstruction

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# currently a long string assigned to variable called belgium

print(Belgium)
print(len(Belgium))
# find out the length of the string of Belgium
print('_' * 81)
# concatenated the hyphen to be multiplied 81 times

print(Belgium.replace(',', ':'))
# you can't use separate function because Belgium is not a list, it's a string. So I have to replace each occurrence of the comma with colon

Belgium_2 = Belgium.split(',')
# this has made Belgium 2 into a list
print(type(Belgium_2))
print(Belgium_2)
print(int(Belgium_2[1]) + int(Belgium_2[3]))
# I have converted the 1st and 3rd arguments into integers and then they have been added together


