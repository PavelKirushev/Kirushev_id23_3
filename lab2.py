from tkinter import *
import random
import time

class Cabbage:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val #размер кустика


class Cabbages:
    def __init__(self, size):
        self.n = 0
        self.size = size
        self.cabbages = []

    def generateCabbage(self, n, goat):
        self.n = n
        cnt = 0
        while cnt < n:
            x = random.randint(50, self.size - 50)
            y = random.randint(50, self.size - 50)
            val = random.randint(5, goat.size * 2)  # размер не больше двойного размера стада чтоб красиво было
            if not self.check_overlap(x, y, val):
                self.cabbages.append(Cabbage(x, y, val))
                cnt += 1

    def appendCabbage(self, goat):
        while True:
            x = random.randint(50, self.size - 50)
            y = random.randint(50, self.size - 50)
            val = random.randint(5, goat.firstSize * 2)
            if not self.check_overlap(x, y, val):
                break
        self.cabbages.append(Cabbage(x, y, val))

    def check_overlap(self, x, y, val):
        for cabbage in self.cabbages:
            distance = ((x - cabbage.x) ** 2 + (y - cabbage.y) ** 2) ** 0.5
            if distance < (val + cabbage.val):
                return True
        return False


class Goat:
    def __init__(self, speed, endurance, eatingSpeed, fertility):
        self.speed = speed
        self.endurance = endurance
        self.eatingSpeed = eatingSpeed
        self.fertility = fertility
        self.x = 0
        self.y = 0
        self.firstSize = 10
        self.size = 10
        self.moveX = 0
        self.moveY = 0
        self.eatingRightNow = False

    def move(self, x, y):
        self.moveX = x
        self.moveY = y
        if self.size > 1: #смерть части стада
            self.size -= 1 / self.endurance

    def eat(self, cabbages, cabbage):
        if cabbage.val > 0:
            cabbage.val -= self.eatingSpeed
            if cabbage.val <= 0:
                cabbages.cabbages.remove(cabbage)
                cabbages.appendCabbage(self)
            self.size += cabbage.val * self.fertility #увеличение после поедания кустика

    def updatePosition(self):
        if self.x != self.moveX or self.y != self.moveY:
            dx = self.moveX - self.x
            dy = self.moveY - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5 #вычисление вектора
            if distance <= self.speed: #в случае когда стадо уже рядом с кустиком
                self.x = self.moveX
                self.y = self.moveY
                self.eatingRightNow = True
            else:
                self.x += dx * self.speed / distance
                self.y += dy * self.speed / distance
                self.eatingRightNow = False

def findNearestCabbage(goat, cabbages):
    nearest = None
    min = 600
    for cabbage in cabbages.cabbages:
        distance = ((goat.x - cabbage.x) ** 2 + (goat.y - cabbage.y) ** 2) ** 0.5
        if distance < min and cabbage.val > 0:
            min = distance
            nearest = cabbage
    return nearest

def update(canvas, goat, cabbages):
    canvas.delete("all")#каждый раз удаляем весь холст и рисуем заново
    for cabbage in cabbages.cabbages:
        canvas.create_oval(cabbage.x - cabbage.val, cabbage.y - cabbage.val,
                           cabbage.x + cabbage.val, cabbage.y + cabbage.val, fill='green')
    if goat.eatingRightNow:
        canvas.create_arc(goat.x - goat.size, goat.y - goat.size,
                           goat.x + goat.size, goat.y + goat.size, start=90, extent=180, fill='gray')
        canvas.create_arc(goat.x - goat.size, goat.y - goat.size,
                          goat.x + goat.size, goat.y + goat.size, start=-90, extent=180, fill='green')
    else:
        canvas.create_oval(goat.x - goat.size, goat.y - goat.size,
                       goat.x + goat.size, goat.y + goat.size, fill='gray')
    root.update()

size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()

goat = Goat(speed=5, endurance=10, eatingSpeed=2, fertility=0.06)
cabbages = Cabbages(size)
cabbages.generateCabbage(20, goat)

while True:
    nearestCabbage = findNearestCabbage(goat, cabbages)
    goat.move(nearestCabbage.x, nearestCabbage.y)
    goat.updatePosition()
    if goat.x == nearestCabbage.x and goat.y == nearestCabbage.y:
        goat.eat(cabbages, nearestCabbage)

    update(canvas, goat, cabbages)
    time.sleep(0.05)#чтобы все было не оч быстро

root.mainloop()