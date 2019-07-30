#!/usr/bin/env python -i
import os
import sys
import re
from re import *
import string as str
from string import *

keyWords = set(['False', 'None', 'True', 'and', 'as', 'assert', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
        'with', 'yield', 'async', 'await'])

fileList = []

statements = input('Enter the file path details to review : ')
with open (statements, 'r') as d:
    data = d.read()
    lines = data.split()
    words = data.strip()
    print('Total line number of the code :: ', len(lines))
    #print(words)
    for i in lines:
        # print(i)
        fileList.append(i)

for item in keyWords:
    if item in fileList:
        print('Found Match :: ', item, enumerate(data))
    else:
        print('Not Found!!!')
