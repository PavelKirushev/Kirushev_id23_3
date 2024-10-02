import tkinter as tk
import math

size = 600
root = tk.Tk()
canvas = tk.Canvas(root, width=size, height=size)
canvas.pack()

x = size // 2
y = size // 2
r = 200
pointR = 10

backCircle = canvas.create_oval(x - r, y - r,
                                       x + r, y + r, fill='blue')
movPoint = canvas.create_oval(x + r - pointR, y - pointR,
                                  x + r + pointR, y + pointR, fill='green')

curAngle = 0
rotSpeed = 0.01
def updPosition():
    global curAngle
    newX = x + r * math.cos(curAngle)
    newY = y + r * math.sin(curAngle)

    canvas.coords(movPoint, newX - pointR, newY - pointR,
                  newX + pointR, newY + pointR)

    curAngle -= rotSpeed
    root.after(10, updPosition)

updPosition()
root.mainloop()