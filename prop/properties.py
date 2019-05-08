#!/usr/bin/emv python -i
import os
import sys
from J_pad import editor

def fileName():
    fContents = editor.notepad
    if fContents == None:
        return None

    else:
        fName = None
