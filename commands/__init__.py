#!/usr/bin/emv python -i
import os
import threading

class thisCommand():
    def new__file(self):
        print('Create a new file as per the requirement')
        # return 'EOF'

    t_new__file = threading.Thread(target=new__file)

    def save__file(self):
        print('save a file')
        # return 'EOF'

    t_save__file = threading.Thread(target=save__file)

    def save_as__file(self):
        print('Save as option for existing file')
        # return 'EOF'

    t_save_as__file = threading.Thread(target=save_as__file)

    def save__all(self):
        print('save all files under an existing folder')
        # return 'EOF'

    t_save__all = threading.Thread(target=save__all)

    def export__html(self):
        print('Export to HTML')
        # return 'EOF'

    t_export__html = threading.Thread(target=export__html)

    def mkFleRdOnly(self):
        print('Make file read only mode')
        # return 'EOF'

    t_mkFleRdOnly = threading.Thread(target=mkFleRdOnly)

    def cut(self):
        print('cut')
        # return 'EOF'

    t_cut = threading.Thread(target=cut)

    def copy(self):
        print('Copy')

    t_copy = threading.Thread(target=copy)

    def clpBrd(self):
        print('Clip board')

    t_clpBrd = threading.Thread(target=clpBrd)

    def paste(self):
        print('paste')

    def delt(self):
        print('Delete!!!')

    def FSM(self):
        print('Full screen mode!!')

    def PsM(self):
        print('Presentation Mode')

    def run(self):
        print('Run this code ::')

    def dbug(self):
        print('Debug this code ::')

    def VBP(self):
        print('View break point')

    def sett(self):
        print('Universal setting')

    def sett__P(self):
        print('Project specified settings')

    def abt(self):
        print('About')

    def fleAnlzer(self):
        print('File analizer')

    def check__code(self):
        print('this method is only for on demand issues')
        # return 'EOF'
