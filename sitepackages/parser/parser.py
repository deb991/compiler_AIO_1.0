#!/usr/bin/env python -i
import os
import sys
import string
import re

class parser():
    def __init__(self):
        pass



    def basicParse(self):
        file = input('Enter file name with PATH~:/>')
        with open(file, 'r') as fileRead:
            data = fileRead.read()
        print(data)
        words = re.findall(r'\bCLASS\b|\bDEF\b', data)
        print(words.gr)



if __name__ == '__main__':
    parseApp = parser()
    parseApp.basicParse()
