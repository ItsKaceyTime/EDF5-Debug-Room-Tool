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

def callback(i,r):
    drop = variables[i]
    drop2 = variables[i+1]
    path = variables[i+2]

    if type(enemylist[drop.get()]) is dict:
        path.config(text = "")
        drop2['values'] = list(enemylist[drop.get()].keys())
        drop2['state'] = "readonly"
    else:
        drop2['values'] = None
        drop2.set("")
        drop2['state'] = "disabled"
        path.config(text = enemylist[drop.get()])
        path.grid(row=r, column=1, padx=10, pady=10)

def filepath(i,r):
    drop = variables[i]
    drop2 = variables[i+1]
    path = variables[i+2]

    path.config(text = enemylist[drop.get()][drop2.get()]["filepath"])
    path.grid(row=r, column=1, padx=10, pady=10)


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

enemydrop1a = ttk.Combobox(master=enemy1frame, values=list(enemylist.keys()), state="readonly")
enemydrop1b = ttk.Combobox(master=enemy1frame, values=[], state="disabled")
enemy1path = tk.Label(master=enemy1frame, text=[])

enemydrop2a = ttk.Combobox(master=enemy2frame, values=list(enemylist.keys()), state="readonly")
enemydrop2b = ttk.Combobox(master=enemy2frame, values=[], state="disabled")
enemy2path = tk.Label(master=enemy2frame, text=[])

enemydrop3a = ttk.Combobox(master=enemy3frame, values=list(enemylist.keys()), state="readonly")
enemydrop3b = ttk.Combobox(master=enemy3frame, values=[], state="disabled")
enemy3path = tk.Label(master=enemy3frame, text=[])

variables = [
    enemydrop1a,
    enemydrop1b,
    enemy1path,
    enemydrop2a,
    enemydrop2b,
    enemy2path,
    enemydrop3a,
    enemydrop3b,
    enemy3path
    ]

enemydrop1a.bind('<<ComboboxSelected>>', lambda i : callback(0,0))
enemydrop1b.bind('<<ComboboxSelected>>', lambda i : filepath(0,0))

enemydrop2a.bind('<<ComboboxSelected>>', lambda i : callback(3,2))
enemydrop2b.bind('<<ComboboxSelected>>', lambda i : filepath(3,2))

enemydrop3a.bind('<<ComboboxSelected>>', lambda i : callback(6,4))
enemydrop3b.bind('<<ComboboxSelected>>', lambda i : filepath(6,4))

enemydrop1a.grid(row=1, column=0, padx=10, pady=10)
enemydrop1b.grid(row=1, column=1, padx=10, pady=10)

enemydrop2a.grid(row=3, column=0, padx=10, pady=10)
enemydrop2b.grid(row=3, column=1, padx=10, pady=10)

enemydrop3a.grid(row=5, column=0, padx=10, pady=10)
enemydrop3b.grid(row=5, column=1, padx=10, pady=10)

window.mainloop()
