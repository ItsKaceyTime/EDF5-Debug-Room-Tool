import tkinter as tk
from tkinter import SUNKEN, ttk
from subprocess import Popen, PIPE
window = tk.Tk()
window.title("Debug Room")
#window.minsize(720,800)
window.resizable(width=False, height=False)

enemylist = {
    "ant" : "app:/OBJECT/GIANTANT01.SGO",
    "frog" : { 
        "basefrog" : {"filepath" : "app:/OBJECT/E503_FROG_AF.SGO"},
        "armor" : {"filepath" : "app:/OBJECT/E503_ARMORFROG_AF.SGO"},
        "leader" : {"filepath" : "app:/OBJECT/E503_FROG_AF_LEADER.SGO"}
    },        
    "spider" : "app:/OBJECT/GIANTSPIDER01.SGO",
    "alien" : {
        "basealien" : {"filepath" : "app:/OBJECT/E506_BIGGREY_AF.SGO"},
        "LL?" : {"filepath" : "app:/OBJECT/E506_BIGGREY_LL.SGO"},
        "leader" : {"filepath" : "app:/OBJECT/E506_BIGGREY_AF_LEADER.SGO"}
    }
}

def callback(i):
    drop = dropwidgets1[i]
    drop2 = dropwidgets2[i]
    path = pathwidgets[i]

    if type(enemylist[drop.get()]) is dict:
        path.config(text = "")
        drop2['values'] = list(enemylist[drop.get()].keys())
        drop2['state'] = "readonly"
    else:
        drop2['values'] = None
        drop2.set("")
        drop2['state'] = "disabled"
        path.config(text = enemylist[drop.get()])
        path.update()

def filepath(i):
    drop = dropwidgets1[i]
    drop2 = dropwidgets2[i]
    path = pathwidgets[i]

    path.config(text = enemylist[drop.get()][drop2.get()]["filepath"])
    path.update()


mainframe = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2)
mainframe.grid()

dropwidgets1=[]
dropwidgets2=[]
pathwidgets=[]
boxwidgets=[]
radiuswidgets=[]
amountwidgets=[]
healthwidgets=[]
intvars=[]

def assignbind1(num):
    dropwidgets1[num].bind('<<ComboboxSelected>>', lambda i : callback(num))

def assignbind2(num):
    dropwidgets2[num].bind('<<ComboboxSelected>>', lambda i : filepath(num))

for num in range(3):
    num2 = num+1
    alt = num+2
    frame = tk.Frame(master=mainframe, relief=tk.GROOVE, borderwidth=2)
    frame.grid(row=num, column=0, sticky="nsew")

    #column 1, dropdown 1
    label = tk.Label(master=frame, text="Enemy "+str(num))
    dropdown = ttk.Combobox(master=frame, name="drop"+str(num), values=list(enemylist.keys()), state="readonly")
    label.grid(row=0, column=0, padx=5, pady=5)
    dropdown.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
    dropdown.current(0)
    dropwidgets1.append(dropdown)
    assignbind1(num)

    #column 2, path and dropdown 2
    label2 = tk.Label(master=frame, name="filepath"+str(num), text="app:/OBJECT/GIANTANT01.SGO", width=40)
    dropdown2 = ttk.Combobox(master=frame, name="drop2"+str(num), values=[], state="disabled")
    label2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
    dropdown2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    dropwidgets2.append(dropdown2)
    pathwidgets.append(label2)
    assignbind2(num)

    #column 3, radius
    label3 = tk.Label(master=frame, text="Radius")
    entry = tk.Entry(master=frame, width=10)
    entry.insert(0, "1.0f")
    label3.grid(row=0, column=2, padx=5, pady=5)
    entry.grid(row=1, column=2, padx=5, pady=5)
    radiuswidgets.append(entry)

    #column 4, amount
    label4 = tk.Label(master=frame, text="Amount")
    entry2 = tk.Entry(master=frame, width=10)
    entry2.insert(0, 1)
    label4.grid(row=0, column=3, padx=5, pady=5)
    entry2.grid(row=1, column=3, padx=5, pady=5)
    amountwidgets.append(entry2)

    #column 5, health
    label5 = tk.Label(master=frame, text="Health %")
    entry3 = tk.Entry(master=frame, width=10)
    entry3.insert(0, "1.0f")
    label5.grid(row=0, column=4, padx=5, pady=5)
    entry3.grid(row=1, column=4, padx=5, pady=5)
    healthwidgets.append(entry3)

    #column 6, aggro
    label6 = tk.Label(master=frame, text="Aggro?")
    isaggro = tk.IntVar()
    intvars.append(isaggro)
    box = ttk.Checkbutton(master=frame, variable=intvars[num], onvalue=1, offvalue=0)
    boxwidgets.append(box)
    label6.grid(row=0, column=5, padx=5, pady=5)
    box.grid(row=1, column=5, padx=5, pady=5)



def button():
    values = {
    "%SPAWN1RADIUSFLOAT%" : radiuswidgets[0].get(),
    "%SPAWN1ENEMYSTRING%" : pathwidgets[0]['text'],
    "%SPAWN1AMOUNTINT%" : amountwidgets[0].get(),
    "%SPAWN1HEALTHFLOAT%" : healthwidgets[0].get(),
    "%SPAWN1AGGROBOOL%" : intvars[0].get(),

    "%SPAWN2RADIUSFLOAT%" : radiuswidgets[1].get(),
    "%SPAWN2ENEMYSTRING%" : pathwidgets[1]['text'],
    "%SPAWN2AMOUNTINT%" : amountwidgets[1].get(),
    "%SPAWN2HEALTHFLOAT%" : healthwidgets[1].get(),
    "%SPAWN2AGGROBOOL%" : intvars[1].get(),

    "%SPAWN3RADIUSFLOAT%" : radiuswidgets[2].get(),
    "%SPAWN3ENEMYSTRING%" : pathwidgets[2]['text'],
    "%SPAWN3AMOUNTINT%" : amountwidgets[2].get(),
    "%SPAWN3HEALTHFLOAT%" : healthwidgets[2].get(),
    "%SPAWN3AGGROBOOL%" : intvars[2].get()
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
            source = source.replace(key, str(values[key]))
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
