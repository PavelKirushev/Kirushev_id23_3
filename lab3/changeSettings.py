import json
from tkinter import ttk
from Goat import *
from Cabbages import *
import tkinter as tk


def isFloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

def openData(fileName):
    with open(fileName, 'r') as file:
        return json.load(file)

def updateData(filename, data, key):
    try:
        with open(filename, "r") as f:
            json_data = json.load(f)
        if isFloat(data):
            json_data[key] = float(data)
        with open(filename, "w") as f:
            json.dump(json_data, f, indent=4)
    except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
        print(f"Error: {e}")


#считываение данных при введедении данных
def change(labelSpeed, entrySpeed, labelEndurance, entryEndurance,
           labelFertility, entryFertility, labelEatingSpeed, entryEatingSpeed, labelCount, entryCount, goat: Goat, cabbages: Cabbages):#функция изменения параматеров при клике на кнопку
    ns = entrySpeed.get()
    if isFloat(ns):
        labelSpeed.config(text="Текущая скорость: " + ns)
        goat.speed = float(ns)
        updateData("data.json", ns, "speed")

    ne = entryEndurance.get()
    if isFloat(ne):
        labelEndurance.config(text="Выносливость: " + ne)
        goat.endurance = float(ne)
        updateData("data.json", ne, "endurance")

    nf = entryFertility.get()
    if isFloat(nf):
        labelFertility.config(text="Плодовитость: " + nf)
        goat.fertility = float(nf)
        updateData("data.json", nf, "fertility")

    nes = entryEatingSpeed.get()
    if isFloat(nes):
        labelEatingSpeed.config(text="Скорость поедания: " + nes)
        goat.eatingSpeed = float(nes)
        updateData("data.json", nes, "eatingSpeed")

    nc = entryCount.get()
    if nc.isdigit():
        nc = int(nc)
        if len(cabbages.cabbages) - nc >= 0:
            for i in range(len(cabbages.cabbages) - nc):
                cabbages.deleteCabbage()
        else:
            for i in range(nc - len(cabbages.cabbages)):
                cabbages.appendCabbage(goat)
        cabbages.n = nc
        updateData("data.json", nc, "countOfCabbages")
    labelCount.config(text="Всего капуст: " + str(cabbages.n))


def entry(parent, goat, cabbages):#создание иконок
    config = openData("data.json")
    labelSpeed = ttk.Label(parent, text=("Текущая скорость: " + str(config["speed"])), width=25)
    labelSpeed.grid(row=0, column=0, sticky=tk.NW, pady=5)
    entrySpeed = ttk.Entry(parent, width=5)
    entrySpeed.grid(row=0, column=1, sticky=tk.NW, padx=10, pady=5)

    labelEndurance = ttk.Label(parent, text=("Выносливость: " + str(config["endurance"])), width=25)
    labelEndurance.grid(row=1, column=0, sticky=tk.NW, pady=5)
    entryEndurance = ttk.Entry(parent, width=5)
    entryEndurance.grid(row=1, column=1, sticky=tk.NW, padx=10, pady=5)

    labelFertility = ttk.Label(parent, text=("Плодовитость: " + str(config["fertility"])), width=25)
    labelFertility.grid(row=2, column=0, sticky=tk.NW, pady=5)
    entryFertility = ttk.Entry(parent, width=5)
    entryFertility.grid(row=2, column=1, sticky=tk.NW, padx=10, pady=5)

    labelEatingSpeed = ttk.Label(parent, text=("Скорость поедания: " + str(config["eatingSpeed"])), width=25)
    labelEatingSpeed.grid(row=3, column=0, sticky=tk.NW, pady=5)
    entryEatingSpeed = ttk.Entry(parent, width=5)
    entryEatingSpeed.grid(row=3, column=1, sticky=tk.NW, padx=10, pady=5)

    labelCount = ttk.Label(parent, text=("Всего капуст: " + str(len(cabbages.cabbages))), width=25)
    labelCount.grid(row=4, column=0, sticky=tk.NW, pady=5)
    entryCount = ttk.Entry(parent, width=5)
    entryCount.grid(row=4, column=1, sticky=tk.NW, padx=10, pady=5)

    btn = ttk.Button(parent, text="Обновить",
                     command=lambda: change(labelSpeed, entrySpeed, labelEndurance, entryEndurance,
                                            labelFertility, entryFertility, labelEatingSpeed, entryEatingSpeed, labelCount, entryCount, goat, cabbages))
    btn.grid(row=5, sticky=tk.NW, padx=10, pady=5)


def newKust(frame, cabbages, event, config):
    labelSpeed = ttk.Label(frame, text=("Размер: "), width=25)
    labelSpeed.grid(row=0, column=0, sticky=tk.NW, pady=5)
    entrySpeed = ttk.Entry(frame, width=5)
    entrySpeed.grid(row=0, column=1, sticky=tk.NW, padx=10, pady=5)

    btn = ttk.Button(frame, text="Ввести",
                     command=lambda: changeNewKust(cabbages, event, labelSpeed, entrySpeed, config, frame))
    btn.grid(row=1, sticky=tk.NW, padx=10, pady=5)
    btn2 = ttk.Button(frame, text="Убрать",
                     command=lambda: frame.grid_forget())
    btn2.grid(row=2, sticky=tk.NW, padx=10, pady=5)

def changeNewKust(cabbages, event, labelSpeed, entrySpeed, config, frame):
        ns = entrySpeed.get()
        if isFloat(ns):
            ns = float(ns)
            cabbages.addCabbage(event.x, event.y, ns)
            cabbages.n += 1
            config["countOfCabbages"] = cabbages.n