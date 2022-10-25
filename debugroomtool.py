import tkinter as tk
from tkinter import ttk
from subprocess import Popen, PIPE
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
    "ant" : "app:/OBJECT/GIANTANT01.SGO",
    "frog" : { 
        "basefrog" : {"filepath" : "app:/OBJECT/E503_FROG_AF.SGO"},
        "armor" : {"filepath" : "app:/OBJECT/E503_ARMORFROG_AF.SGO"},
        "leader" : {"filepath" : "app:/OBJECT/E503_FROG_AF_LEADER.SGO"}
    },        
    "spider" : "app:/OBJECT/GIANTSPIDER01.SGO",
    "alien" : {
        "basealien" : {"filepath" : "app:/OBJECT/BIGGREY_AF.SGO"},
        "LL?" : {"filepath" : "app:/OBJECT/BIGGREY_LL.SGO"},
        "leader" : {"filepath" : "app:/OBJECT/BIGGREY_AF_LEADER.SGO"}
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
        path.grid(row=r, column=1, padx=10, pady=10, sticky="nsew")

def filepath(i,r):
    drop = variables[i]
    drop2 = variables[i+1]
    path = variables[i+2]

    path.config(text = enemylist[drop.get()][drop2.get()]["filepath"])
    path.grid(row=r, column=1, padx=10, pady=10)


mainframe = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2)
mainframe.grid()

enemy1frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
enemy1frame.grid(row=0,column=0, sticky="nsew")
enemy1label = tk.Label(master=enemy1frame, text=labeltext[0])
enemy1label.grid(row=0, column=0, pady=10)

enemy2frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
enemy2frame.grid(row=2, column=0, sticky="nsew")
enemy2label = tk.Label(master=enemy2frame, text=labeltext[1])
enemy2label.grid(row=2, column=0, pady=10)

enemy3frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
enemy3frame.grid(row=4, column=0, sticky="nsew")
enemy3label = tk.Label(master=enemy3frame, text=labeltext[2])
enemy3label.grid(row=4, column=0, pady=10)

enemydrop1a = ttk.Combobox(master=enemy1frame, values=list(enemylist.keys()), state="readonly")
enemydrop1a.current(0)
enemydrop1b = ttk.Combobox(master=enemy1frame, values=[], state="disabled")
enemy1path = tk.Label(master=enemy1frame, text="app:/OBJECT/GIANTANT01.SGO")

enemydrop2a = ttk.Combobox(master=enemy2frame, values=list(enemylist.keys()), state="readonly")
enemydrop2a.current(0)
enemydrop2b = ttk.Combobox(master=enemy2frame, values=[], state="disabled")
enemy2path = tk.Label(master=enemy2frame, text="app:/OBJECT/GIANTANT01.SGO")

enemydrop3a = ttk.Combobox(master=enemy3frame, values=list(enemylist.keys()), state="readonly")
enemydrop3a.current(0)
enemydrop3b = ttk.Combobox(master=enemy3frame, values=[], state="disabled")
enemy3path = tk.Label(master=enemy3frame, text="app:/OBJECT/GIANTANT01.SGO")

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

enemydrop1a.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
enemydrop1b.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
enemy1path.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
enemydrop2a.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
enemydrop2b.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
enemy2path.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
enemydrop3a.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
enemydrop3b.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
enemy3path.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

def button():

    values = {
    "%SPAWN1RADIUSFLOAT%" : "1.0f",
    "%SPAWN1ENEMYSTRING%" : enemy1path['text'],
    "%SPAWN1AMOUNTINT%" : "1",
    "%SPAWN1HEALTHFLOAT%" : "1.0f",
    "%SPAWN1AGGROBOOL%" : "1",

    "%SPAWN2RADIUSFLOAT%" : "1.0f",
    "%SPAWN2ENEMYSTRING%" : enemy2path['text'],
    "%SPAWN2AMOUNTINT%" : "1",
    "%SPAWN2HEALTHFLOAT%" : "1.0f",
    "%SPAWN2AGGROBOOL%" : "1",

    "%SPAWN3RADIUSFLOAT%" : "1.0f",
    "%SPAWN3ENEMYSTRING%" : enemy3path['text'],
    "%SPAWN3AMOUNTINT%" : "1",
    "%SPAWN3HEALTHFLOAT%" : "1.0f",
    "%SPAWN3AGGROBOOL%" : "1"
    }
    
    global window2
    window2 = tk.Toplevel(master=mainframe)
    window2.title = "Finished"
    window2.resizable(width=False, height=False)
    x = window.winfo_x()
    y = window.winfo_y()
    window2.geometry("+%d+%d" %(x+200,y+200))
    window2.wm_transient(window)
    window2.grid()
    popupframe = tk.Frame(master=window2)
    popuplabel = tk.Label(master=popupframe, text="Finished! Check the .exe's folder.")
    closebutton = tk.Button(master=popupframe, text="Close", relief=tk.GROOVE, borderwidth=5, command=popupdestroy)
    confirm['state'] = "disabled"
    popupframe.grid(sticky="nsew")
    popuplabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    closebutton.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    window2.protocol("WM_DELETE_WINDOW", popupdestroy)
    with open('dummy.txt', 'r', encoding="utf_16_be") as f:
        source = f.read()
        for key in values.keys():
            source = source.replace(key, values[key])
    with open('MISSION.txt', 'w', encoding="utf_16_be") as f:
        f.write(source)
    p = Popen(["EDF Tools.exe", "MISSION.txt"], stdin=PIPE, shell=True)
    p.communicate(input=b'\n')

def popupdestroy():
    confirm['state'] = "normal"
    window2.destroy()

confirm = tk.Button(master=mainframe, text="Confirm", relief=tk.GROOVE, borderwidth=5, command=button)
confirm.grid(row=6, column=0, sticky="nsew")

window.mainloop()
