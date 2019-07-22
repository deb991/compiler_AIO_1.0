#!/usr/bin/emv python
import os
import sys
import string
import re

predefined_keywords = ['class', 'def', 'import', 'from']
user_defined_keywords = ['#']
new_modified_list = []
line_number = 1

f1 = input('Enter file name with directory details ::')

for word in predefined_keywords:
    words = word
    print(words)

    if os.path.isfile(f1):
        with open(f1, 'r') as data:
            for line in data:
                for m in re.finditer(r'\bnotebook\b', line):
                    print(m.group())
                    line_number += 1
                    c = re.compile(r"\bimport\b | \bfrom\b | \bclass\b | \bnotebook\b", flags=re.I | re.X)
                    c.findall(line)
                    print('This is second flag ::', c.findall(line))
                    m = re.search('(.*)(?<=notebook)(.*)', line)
                    if m is not None:
                        m.group(0)
                        # print('Found it.')
                        print(m.group())
                        print("Found", m.group(0), "line", line_number,
                              "at", m.start(), "-", m.end())
