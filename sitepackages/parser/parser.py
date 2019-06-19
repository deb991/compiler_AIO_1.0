#!/usr/bin/env python -i
import os
import sys
import string
import re
from collections import Counter

file_save_to = (os.getcwd())
file_name = input('Enter file name to save :: ')
compFileName = os.path.join(file_save_to, file_name+"__tokenized.txt")
tokenized__file = open(compFileName, 'w')


print('\nEnter file with path to PARSE & tokenize ::')
filePath = input('::/>')

with open(filePath, 'r') as file:
    data = file.read()
    lines = data.splitlines()


    for line in lines:
        sys.stdout = tokenized__file
        print('Charecter numbers as per Line numbers. :: ', + len(line))
        sys.stdout.close()

words = Counter(filePath)        ##Counting each of the word from the source file.
sys.stdout = (tokenized__file, "a+")
print('Words per Line :: ', words)  ## Flag Ver #2
#sys.stdout.close()

char__count = Counter(filePath)
sys.stdout = (tokenized__file, 'a+')
print("Charecters count within:: ", + char__count) ##Flag ver #3
#sys.stdout.close()



#try:
#    print('\nEnter file with path to PARSE & tokenize ::')
#    filePath = input('::/>')
#    with open(filePath, 'r') as reading:
#        s = reading.read()
#        lines = s.splitlines()
#        words = s.splitlines()
#
#
#        for line in lines:
#                sys.stdout = tokenized__file.write()
#                print('Charecter numbers as per Line numbers. :: ', + len(line))  ## Flag Ver #1
#                tokenized__file.close()
#except:
#    print('File not found!!!')
#
#print('EOF')
