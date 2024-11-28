from Cabbages import *
from Goat import *
from tkinter import ttk
import tkinter as tk

#добавление козла со всем функционалом(параметры)
def AddGoat(button, root, config, goats):

    def TakeValues():
        try:
            s = int(spinboxSpeed.get())
            e = int(spinboxEndurance.get())
            f = int(spinboxFertility.get())
        except ValueError:
            s = config["speed"]
            e = config["endurance"]
            f = config["fertility"]
        goat = Goat(s, e, config["eatingSpeed"], f)
        if goats.goats[0].paused:
            goat.paused = True
        goats.add(goat)

    add = ttk.Button(root, text="Ввести",
                     command=lambda: TakeValues())
    add.grid(row=4, column=0, sticky=tk.NW, padx=10, pady=5)

    speed = [i for i in range(0, 11)]
    endurance = [i for i in range(0, 51, 2)]
    fertility = [i for i in range(0, 101, 5)]

    spinboxSpeed = ttk.Spinbox(root, from_=1.0, to=100.0, width=5, values=speed, wrap=True, state="readonly")
    spinboxEndurance = ttk.Spinbox(root, from_=1.0, to=100.0, width=5, values=endurance, wrap=True, state="readonly")
    spinboxFertility = ttk.Spinbox(root, from_=1.0, to=100.0, width=5, values=fertility, wrap=True, state="readonly")

    labelSpeed = ttk.Label(root, text=("Введите скорость: "), width=25)
    labelEndurance = ttk.Label(root, text=("Введите выносливость: "), width=25)
    labelFertility = ttk.Label(root, text=("Введите рождаемость: "), width=25)
    if button.cget('text') == "Добавить стадо":
        button.config(text="Убрать меню")
        root.grid(row=0, column=0, sticky=tk.NS)
        spinboxSpeed.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)
        spinboxEndurance.grid(row=2, column=1, sticky=tk.NW, padx=10, pady=5)
        spinboxFertility.grid(row=3, column=1, sticky=tk.NW, padx=10, pady=5)

        labelSpeed.grid(row=1, column=0, sticky=tk.NW, pady=5)
        labelEndurance.grid(row=2, column=0, sticky=tk.NW, pady=5)
        labelFertility.grid(row=3, column=0, sticky=tk.NW, pady=5)
    else:
        root.grid_forget()
        button.config(text="Добавить стадо")