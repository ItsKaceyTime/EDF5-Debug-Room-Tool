import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Debug Room")
#window.minsize(720,800)
window.resizable(width=False, height=False)

labeltext = [
    "enemy 1:",
    "enemy 2:",
    "enemy 3:"
]

enemylist = {
    "frog" : { 
        "basefrog" : {"filepath" : "FROGFILEPATH"},
        "armor" : {"filepath" : "FROGARMORFILEPATH"},
        "leader" : {"filepath" : "FROGLEADERFILEPATH"}
    },        
    "ant" : "ANTFILEPATH",
    "spider" : "SPIDERFILEPATH",
    "alien" : {
        "basealien" : {"filepath" : "ALIENFILEPATH"},
        "armor" : {"filepath" : "ALIENARMORPATH"},
        "leader" : {"filepath" : "ALIENLEADERPATH"}
    }
}

def callback1(value):
    if type(enemylist[enemyentry1a.get()]) is dict:
        enemy1path.config(text = "")
        enemyentry1b['values'] = list(enemylist[enemyentry1a.get()].keys())
        enemyentry1b['state'] = "readonly"
    else:
        enemyentry1b['values'] = None
        enemyentry1b.set("")
        enemyentry1b['state'] = "disabled"
        enemy1path.config(text = enemylist[enemyentry1a.get()])
        enemy1path.grid(row=0, column=1, padx=10, pady=10)

def filepath1(value):
    enemy1path.config(text = enemylist[enemyentry1a.get()][enemyentry1b.get()]["filepath"])
    enemy1path.grid(row=0, column=1, padx=10, pady=10)

def callback2(value):
    if type(enemylist[enemyentry2a.get()]) is dict:
        enemy2path.config(text = "")
        enemyentry2b['values'] = list(enemylist[enemyentry2a.get()].keys())
        enemyentry2b['state'] = "readonly"
    else:
        enemyentry2b['values'] = None
        enemyentry2b.set("")
        enemyentry2b['state'] = "disabled"
        enemy2path.config(text = enemylist[enemyentry2a.get()])
        enemy2path.grid(row=2, column=1, padx=10, pady=10)

def filepath2(value):
    enemy2path.config(text = enemylist[enemyentry2a.get()][enemyentry2b.get()]["filepath"])
    enemy2path.grid(row=2, column=1, padx=10, pady=10)

def callback3(value):
    if type(enemylist[enemyentry3a.get()]) is dict:
        enemy3path.config(text = "")
        enemyentry3b['values'] = list(enemylist[enemyentry3a.get()].keys())
        enemyentry3b['state'] = "readonly"
    else:
        enemyentry3b['values'] = None
        enemyentry3b.set("")
        enemyentry3b['state'] = "disabled"
        enemy3path.config(text = enemylist[enemyentry2a.get()])
        enemy3path.grid(row=4, column=1, padx=10, pady=10)

def filepath3(value):
    enemy3path.config(text = enemylist[enemyentry3a.get()][enemyentry3b.get()]["filepath"])
    enemy3path.grid(row=4, column=1, padx=10, pady=10)

mainframe = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2)
mainframe.grid()

enemy1frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
enemy1frame.grid(row=0,column=0)
enemy1label = tk.Label(master=enemy1frame, text=labeltext[0])
enemy1label.grid(row=0, column=0, pady=10)

enemy2frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
enemy2frame.grid(row=2, column=0)
enemy2label = tk.Label(master=enemy2frame, text=labeltext[1])
enemy2label.grid(row=2, column=0, pady=10)

enemy3frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
enemy3frame.grid(row=4, column=0)
enemy3label = tk.Label(master=enemy3frame, text=labeltext[2])
enemy3label.grid(row=4, column=0, pady=10)

enemyentry1a = ttk.Combobox(master=enemy1frame, values=list(enemylist.keys()), state="readonly")
enemyentry1b = ttk.Combobox(master=enemy1frame, values=[], state="disabled")
enemy1path = tk.Label(master=enemy1frame, text=[])

enemyentry2a = ttk.Combobox(master=enemy2frame, values=list(enemylist.keys()), state="readonly")
enemyentry2b = ttk.Combobox(master=enemy2frame, values=[], state="disabled")
enemy2path = tk.Label(master=enemy2frame, text=[])

enemyentry3a = ttk.Combobox(master=enemy3frame, values=list(enemylist.keys()), state="readonly")
enemyentry3b = ttk.Combobox(master=enemy3frame, values=[], state="disabled")
enemy3path = tk.Label(master=enemy3frame, text=[])

enemyentry1a.bind('<<ComboboxSelected>>', callback1)
enemyentry1b.bind('<<ComboboxSelected>>', filepath1)

enemyentry2a.bind('<<ComboboxSelected>>', callback2)
enemyentry2b.bind('<<ComboboxSelected>>', filepath2)

enemyentry3a.bind('<<ComboboxSelected>>', callback3)
enemyentry3b.bind('<<ComboboxSelected>>', filepath3)

enemyentry1a.grid(row=1, column=0, padx=10, pady=10)
enemyentry1b.grid(row=1, column=1, padx=10, pady=10)

enemyentry2a.grid(row=3, column=0, padx=10, pady=10)
enemyentry2b.grid(row=3, column=1, padx=10, pady=10)

enemyentry3a.grid(row=5, column=0, padx=10, pady=10)
enemyentry3b.grid(row=5, column=1, padx=10, pady=10)

#testlabel = tk.Label(master=mainframe, text=labeltext[0])
#testlabel.grid(row=0, column=0, sticky="nsew")

#for index, label in enumerate(labeltext):
#    frame = tk.Frame(
#        master=mainframe,
#        relief=tk.GROOVE,
#        borderwidth=1
#    )
#    frame.grid(row=index, column=index)
#    gridlabel = tk.Label(master=frame, text=str(frame.row, frame.column))



window.mainloop()
