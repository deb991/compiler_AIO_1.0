#!/usr/bin/emv python -i
import os
import threading
#import console
import subprocess


def new__file():
    print('Create a new file as per the requirement')
    # return 'EOF'


t_new__file = threading.Thread(target=new__file)


def save__file():
    print('save a file')
    # return 'EOF'


t_save__file = threading.Thread(target=save__file)


def save_as__file():
    print('Save as option for existing file')
    # return 'EOF'


t_save_as__file = threading.Thread(target=save_as__file)


def save__all():
    print('save all files under an existing folder')
    # return 'EOF'


t_save__all = threading.Thread(target=save__all)


def export__html():
    print('Export to HTML')
    # return 'EOF'


t_export__html = threading.Thread(target=export__html)


def mkFleRdOnly():
    print('Make file read only mode')
    # return 'EOF'


t_mkFleRdOnly = threading.Thread(target=mkFleRdOnly)


def cut():
    print('cut')
    # return 'EOF'


t_cut = threading.Thread(target=cut)


def copy():
    print('Copy')


t_copy = threading.Thread(target=copy)


def clpBrd():
    print('Clip board')


t_clpBrd = threading.Thread(target=clpBrd)


def paste():
    print('paste')


def delt():
    print('Delete!!!')


def FSM():
    print('Full screen mode!!')


def PsM():
    print('Presentation Mode')


def run():
    os.system('python -m <Control-A>')
    print('Run this code ::')



def dbug():
    import pdb
    from pdb import set_trace
    print('Debug this code ::')



def VBP():
    print('View break point')


def sett():
    print('Universal setting')


def sett__P():
    print('Project specified settings')


def abt():
    print('About')


def fleAnlzer():
    print('File analizer')


def check__code():
    print('this method is only for on demand issues')
    # return 'EOF'

def console_in_cmd():
    os.system("start /wait cmd /c {os.getcwd()}")


def f__Manager():
    try:
        from Tkinter import Tk
    except ImportError:
        from tkinter import Tk
    from idlelib.tree import FileTreeItem, ScrolledCanvas, TreeNode, _tree_widget
    import os
    root = Tk( )
    root.title("Test TreeWidget")
    sc = ScrolledCanvas(root, bg="white", highlightthickness=0, takefocus=1)
    sc.frame.pack(expand=1, fill="both", side="left")
    item = FileTreeItem(os.getcwd( ))
    node = TreeNode(sc.canvas, None, item)
    node.expand( )
    root.mainloop( )

t__f_manager = threading.Thread(target=f__Manager)

