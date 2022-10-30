import os.path
import json
import shutil
import tkinter as tk
from tkinter import SUNKEN, ttk, filedialog
from subprocess import Popen, PIPE

with open("enemylist.json", "r") as f:
    ENEMYLIST = json.load(f)

class TargetConfiguration(tk.Frame):
    def __init__(self, **kwargs):
        self.fp = None
        self.amount = None
        self.radius = None
        self.health = None
        self.aggro = None

        # Pass the constructor to tk.Frame.__init__() in order to get a normal tk.Frame outwards
        super().__init__(**kwargs)
        self._speciespicker = None
        self._variantpicker = None

    def construct(self, num):
        self.fp = tk.StringVar(self, "app:/OBJECT/GIANTANT01.SGO")
        self.amount = tk.StringVar(self, "1")
        self.radius = tk.StringVar(self, "1.0")
        self.health = tk.StringVar(self, "1.0")
        self.aggro = tk.StringVar(self, "1.0")
        self.aggro = tk.IntVar(self, 0)

        # Generate labels in order; the 2nd one needs special treatment :<
        for i, t in enumerate([f"Enemy {num}", "", "Radius", "Amount", "Health", "Aggro"]):
            L = tk.Label(master=self, text=t)
            L.grid(row=0, column=i, padx=5, pady=5)
            if i == 1: # Unique case. This label updates programmatically
                L['textvariable'] = self.fp
                L['width'] = 50

        # Instanciate the species pickers and add them to the class instance
        self._speciespicker = ttk.Combobox(master=self, values=list(ENEMYLIST.keys()), state="readonly")
        self._speciespicker.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self._speciespicker.current(5) # Default option to show in UI, Counted as speciespicker
        self._speciespicker.bind('<<ComboboxSelected>>', self.selectionMade)
        # Same thing for the variant pickers. Get a snack, you deserve it.
        self._variantpicker = ttk.Combobox(master=self, values=[], state="disabled")
        self._variantpicker.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        self._variantpicker.bind('<<ComboboxSelected>>', self.selectionMade)

        # Generate numerical inputs. Their position to .grid() is offset by 2 to account for species and variant pickers.
        for i, v in enumerate([self.amount, self.radius, self.health]):
            entry = tk.Entry(master=self, width=10, textvariable=v)
            entry.grid(row=1, column=i+2, padx=5, pady=5)

        # And one little checkbox for the aggro boolean.
        box = ttk.Checkbutton(master=self, variable=self.aggro)
        box.grid(row=1, column=5, padx=5, pady=5)

    def selectionMade(self, e):
        try:
            if isinstance(ENEMYLIST[e.widget.get()], dict):
                self._variantpicker['values'] = list(ENEMYLIST[e.widget.get()].keys())
                self._variantpicker['state'] = "readonly"
                self.fp.set("")
            else:
                self._variantpicker['values'] = None
                self._variantpicker.set("")
                self._variantpicker['state'] = "disabled"
                self.fp.set(ENEMYLIST[self._speciespicker.get()])
        except KeyError:
            # Variants are not outlined, so KeyError means a variant was selected.
            self.fp.set(ENEMYLIST[self._speciespicker.get()][self._variantpicker.get()])

def popup(title, text, block):
    def popupdestroy():
        block['state'] = "normal"
        window2.destroy()
    window2 = tk.Toplevel(master=mainframe)
    window2.title = title
    window2.resizable(width=False, height=False)
    x = window.winfo_x()
    y = window.winfo_y()
    window2.geometry("+%d+%d" %(x+200,y+200))
    window2.wm_transient(window)
    window2.grid()
    popupframe = tk.Frame(master=window2)
    popuplabel = tk.Label(master=popupframe, text=text)
    closebutton = tk.Button(master=popupframe, text="Close", relief=tk.GROOVE, borderwidth=5, command=popupdestroy)
    block['state'] = "disabled"
    popupframe.grid(sticky="nsew")
    popuplabel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    closebutton.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    window2.protocol("WM_DELETE_WINDOW", popupdestroy)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Debug Room")
    #window.minsize(720,800)
    window.resizable(width=False, height=False)

    mainframe = tk.Frame(master=window, relief=tk.GROOVE, borderwidth=2)
    mainframe.grid()

    ShootingTargets = []
    for i in range(3):
        frame = TargetConfiguration(master=mainframe, relief=tk.GROOVE, borderwidth=2)
        frame.construct(i)
        frame.grid(row=i, column=0, sticky="nsew")
        ShootingTargets.append(frame)

    def button():
        string_replacements = {}
        for index, ShootingTarget in enumerate(ShootingTargets):
            string_replacements[f"%SPAWN{index+1}RADIUSFLOAT%"] = ShootingTarget.radius.get()
            string_replacements[f"%SPAWN{index+1}ENEMYSTRING%"] = ShootingTarget.fp.get()
            string_replacements[f"%SPAWN{index+1}AMOUNTINT%"] = int(ShootingTarget.amount.get())
            string_replacements[f"%SPAWN{index+1}HEALTHFLOAT%"] = f"{ShootingTarget.health.get()}f"
            string_replacements[f"%SPAWN{index+1}AGGROBOOL%"] = f"{ShootingTarget.aggro.get()}f"
        
        try:
            with open('template.txt', 'r', encoding="utf_16_be") as f:
                source = f.read()
                for dummy, value in string_replacements.items():
                    source = source.replace(dummy, str(value))
        except FileNotFoundError:
            popup("Error!", "template.txt not found.", confirm)
        with open('MISSION.txt', 'w', encoding="utf_16_be") as f:
            f.write(source)
        if (os.path.isfile("EDF Tools.exe")):
            with Popen(["EDF Tools.exe", "MISSION.txt"], stdin=PIPE, shell=True) as p:
                popup("Complete!", "Mission file written.", confirm)
                p.communicate(input=b'\n')
                if outputdir.get() != "":
                    shutil.move("./MISSION.bvm", os.path.join(outputdir.get(), "MISSION.bvm"))
        else:
            popup("Error!", "Could not find EDF Tools.exe", confirm)
    #bottom options
    def browse_output():
        outputdir.set(filedialog.askdirectory())
    f = tk.Frame(master=mainframe)
    f.columnconfigure(1, weight=1)
    outputdir = tk.StringVar(f, "")
    tk.Label(master=f, text="Output Directory:").grid(row=0, column=0, padx=5, sticky="w")
    tk.Entry(master=f, textvariable=outputdir).grid(row=0, column=1, sticky="ew")
    tk.Button(master=f, text="Browse", command=browse_output).grid(row=0, column=2, padx=5, sticky="e")
    confirm = tk.Button(master=mainframe, text="Confirm", relief=tk.GROOVE, borderwidth=5, command=button)
    f.grid(row=4, column=0, pady=5, sticky="ew")
    confirm.grid(row=5, column=0, sticky="nsew")

    window.mainloop()
