#!/usr/bin/env python -i
import os
import tkinter as tk
from tkinter import *
import fnmatch

keyWords = ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
        'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
        'with', 'yield', 'async', 'await']

fileList = []
module_list = []

statements = input('Enter the file path details to review : ')

def codeChecking():
    with open(statements, 'r') as d:
        data = d.read()
        lines = data.splitlines()
        words = data.split()
        print('Total line number of the code :: ', len(lines))
        # print(words)
        for i in words:
            # print(i)
            fileList.append(i)

    for item in keyWords:
        if item in fileList:
            print('Found Match :: ', item, '\t >> Line Number:: ', enumerate(data))
        else:
            print('Not Found!!!')

pattern = input('Enter file types to be search\t::\t')
path = input('Enter the path, where need to check\t ::\t')

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    print(result)


codeChecking()
find(pattern, path)

