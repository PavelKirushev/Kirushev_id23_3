from tkinter import *
from changeSettings import *
from AddGoat import *
import time

def update(canvas, goats, cabbages, root, nearestCabbage):
    canvas.delete("all")  # каждый раз удаляем весь холст и рисуем заново
    flag = False
    for goat in goats.goats:
        if goat.eatingRightNow:
            flag = True
            canvas.create_arc(goat.x - goat.size, goat.y - goat.size,
                              goat.x + goat.size, goat.y + goat.size, start=90, extent=180, fill='gray')
            canvas.create_arc(nearestCabbage.x - nearestCabbage.val, nearestCabbage.y - nearestCabbage.val,
                              nearestCabbage.x + nearestCabbage.val, nearestCabbage.y + nearestCabbage.val, start=-90, extent=180, fill='green')
        else:
            flag = False
            canvas.create_oval(goat.x - goat.size, goat.y - goat.size,
                               goat.x + goat.size, goat.y + goat.size, fill='gray')
    for cabbage in cabbages.cabbages:
        if (cabbage == nearestCabbage) and flag and cabbage.eatenRightNow:
            continue
        canvas.create_oval(cabbage.x - cabbage.val, cabbage.y - cabbage.val,
                           cabbage.x + cabbage.val, cabbage.y + cabbage.val, fill='green')
    root.update()



def on_click(event, cabbages, config, frame):
    newKust(frame, cabbages, event, config)
    frame.grid(row=0, column=0, sticky=tk.NS)

def toggle_menu(button, goat, cabbages, control_frame):
    # Функция для показа/скрытия меню
    if button.cget('text') == "Параметры":
        control_frame.grid(row=0, column=0, sticky=tk.NS)  # Показать меню
        entry(control_frame, goat, cabbages)
        button.config(text="Убрать")
    else:
        control_frame.grid_forget()  # Убрать меню
        button.config(text="Параметры")

def stop(button, goats):
    if button.cget('text') == "Пауза":
        button.config(text="Старт")
        for goat in goats.goats:
            goat.paused = True  # Use a paused flag to stop movement
    else:
        button.config(text="Пауза")
        for goat in goats.goats:
            goat.paused = False

def endProg(root, canvas):
    canvas.quit()
    canvas.destroy()
    root.quit()
    root.destroy()

def start():
    config = openData("data.json")


    goat = Goat(config["speed"], config["endurance"], config["eatingSpeed"], config["fertility"])
    cabbages = Cabbages(config["screenWidth"], config["screenHeight"])
    cabbages.generateCabbage(config["countOfCabbages"], goat)
    goats = Goats(goat)
    # Главное окно
    root = Tk()
    root.title("Козы и капусты")


    left_frame = Frame(root, width=200, height=200, bg="lightgray",)  # фрейм для отображения параметров первичного стада
    right_frame = Frame(root, width=200, height=200, bg="lightgray") # фрейм для отображения параметров при создании нового стада
    new_frame = Frame(root, width=200, height=200, bg="lightgray")
    canvas_frame = Frame(root, width=config["screenWidth"] + 200, height=config["screenHeight"])# основной фрейм
    canvas_frame.grid(row=0, column=3, sticky=tk.NSEW)


    canvas = Canvas(canvas_frame, width=config["screenWidth"], height=config["screenHeight"], bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.bind("<Button-1>", lambda event: on_click(event, cabbages, config, new_frame))


    b = ttk.Button(root, text="Параметры",
                   command=lambda: toggle_menu(b, goat, cabbages, left_frame), width= 20)
    b.grid(row=4, column=0, padx=10, pady=5)

    add = ttk.Button(root, text="Добавить стадо",
                   command=lambda: AddGoat(add, right_frame, config, goats), width= 20)
    add.grid(row=5, column=0, padx=10, pady=5)

    pause = ttk.Button(root, text="Пауза",
                   command=lambda: stop(pause, goats), width= 20)
    pause.grid(row=6, column=0, padx=10, pady=5)

    end = ttk.Button(root, text="Завершить",
                       command=lambda: endProg(root, canvas), width=20)
    end.grid(row=6, column=3, sticky=E, padx=10, pady=5)

    # Главный цикл
    while True:
        for goat in goats.goats:
            nearestCabbage = findNearestCabbage(goat, cabbages)
            goat.updatePosition()
            if goat.x == nearestCabbage.x and goat.y == nearestCabbage.y:
                nearestCabbage.eatenRightNow = True
                goat.eat(cabbages, nearestCabbage)

            update(canvas, goats, cabbages, root, nearestCabbage)
            goat.move(nearestCabbage.x, nearestCabbage.y)
        if len(goats.goats) == 1:
            time.sleep(0.05)
        elif len(goats.goats) == 2:
            time.sleep(0.047)
        elif len(goats.goats) == 3:
            time.sleep(0.045)
        else:
            time.sleep(0.04)

    root.mainloop()


start()
