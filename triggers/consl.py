#!/usr/bin/env python
import subprocess
from console import *

cmd = 'python C:\\Users\\DE635273\\PycharmProjects\\Compiler__0.0.1\\console\\__init__.py'

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
out, err = p.communicate()
result = out.split('\n')
for lin in result:
    if not lin.startswith('#'):
        print(lin)
