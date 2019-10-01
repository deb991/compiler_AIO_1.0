import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

main = tk.Tk()
main.resizable(False, False)
main.attributes('-fullscreen', True)
main.configure(background="#253042")
rows = 0
style = ttk.Style()
style.theme_create("body", parent="alt", settings={
    "TNotebook": {"configure": {"tabmargins": [7, 5, 2, 0], "background": "#253042"}},
    "TNotebook.Tab": {
        "configure": {"padding": [5, 1], "background": "#253042", "foreground": "white"},
        "map": {"background": [("selected", "black")],
                "expand": [("selected", [2, 3, 3, 0])]}
    },
    "TProgressbar": {"configure": {"background": "orange", "troughcolor": "#253042", "borderwidth": "5"}}
}
                   )

style.theme_use("body")
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
ttk.Style().configure('My.TFrame', background="#253042")
tab = ttk.Notebook(main)
tab.grid(row=2, column=0, columnspan=50, rowspan=49, sticky='NESW')
tab1 = ttk.Frame(tab, style='My.TFrame')
tab.add(tab1, text='Tab1')


def new():
    tab2 = ttk.Frame(tab, style='My.TFrame')
    tab.add(tab2, text='New Tab')


nb = ttk.Notebook(tab1)
tk.Button(main, text="New", background='black', foreground='white', command=new).grid(row=0, column=46, padx=2, pady=0,
                                                                                      sticky='NESW')
tk.Button(main, text="Load", background='black', foreground='white').grid(row=0, column=47, padx=(1, 10), pady=0,
                                                                          sticky='NESW')
tk.Button(main, text="-", command=main.iconify, background='black', foreground='white').grid(row=0, column=48, padx=0,
                                                                                             pady=0, sticky='NESW')
tk.Button(main, text="X", command=main.destroy, background='black', foreground='white').grid(row=0, column=49, padx=0,
                                                                                             pady=0, sticky='NESW')
nb.grid(row=0, column=0, columnspan=50, rowspan=49, sticky='NESW')

page1 = ttk.Frame(nb, style='My.TFrame')
nb.add(page1, text='Scanning')

rows = 0
while rows < 50:
    tab1.rowconfigure(rows, weight=1)
    tab1.columnconfigure(rows, weight=1)
    rows += 1

page2 = ttk.Frame(nb, style='My.TFrame')
nb.add(page2, text='Imagine')

page3 = ttk.Frame(nb, style='My.TFrame')
nb.add(page3, text='Impurity')

page4 = ttk.Frame(nb, style='My.TFrame')
nb.add(page4, text='Marking')

main.mainloop()
