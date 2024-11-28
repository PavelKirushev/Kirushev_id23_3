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
        self.paused = False

    def move(self, x, y):
        if not self.paused:
            self.moveX = x
            self.moveY = y
            if self.size > 1: #смерть части стада
                self.size -= 1 / self.endurance

    def eat(self, cabbages, cabbage):
        if not self.paused:
            if cabbage.val > 0:
                cabbage.val -= self.eatingSpeed
                if cabbage.val <= 0:
                    cabbages.cabbages.remove(cabbage)
                    cabbages.appendCabbage(self)
                if self.eatingSpeed != 0:
                    self.size += cabbage.val * (self.fertility * 0.001) #увеличение после поедания кустика

    def updatePosition(self):
        if not self.paused:
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

class Goats:
    def __init__(self, goat):
        self.n = 1
        self.goats = [goat]


    def add(self, goat):
        self.goats.append(goat)