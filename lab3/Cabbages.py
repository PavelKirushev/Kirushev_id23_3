import random

class Cabbage:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val #размер кустика
        self.eatenRightNow = False


class Cabbages:
    def __init__(self, weight, height):
        self.n = 0
        self.weight = weight
        self.height = height
        self.cabbages = []

    def generateCabbage(self, n, goat):
        self.n = n
        cnt = 0
        while cnt < n:
            x = random.randint(50, self.weight - 50)
            y = random.randint(50, self.height - 50)
            val = random.randint(5, goat.size * 2)  # размер не больше двойного размера стада чтоб красиво было
            if not self.check_overlap(x, y, val):
                self.cabbages.append(Cabbage(x, y, val))
                cnt += 1

    def appendCabbage(self, goat):
        while True:
            x = random.randint(50, self.weight - 50)
            y = random.randint(50, self.height - 50)
            val = random.randint(5, goat.firstSize * 2)
            if not self.check_overlap(x, y, val):
                break
        self.cabbages.append(Cabbage(x, y, val))

    def addCabbage(self, x, y, val):
        self.cabbages.append(Cabbage(x, y, val))


    def deleteCabbage(self):
        self.cabbages.pop()

    def check_overlap(self, x, y, val):
        for cabbage in self.cabbages:
            distance = ((x - cabbage.x) ** 2 + (y - cabbage.y) ** 2) ** 0.5
            if distance < (val + cabbage.val):
                return True
        return False

def findNearestCabbage(goat, cabbages):
    nearest = None
    min = 600
    for cabbage in cabbages.cabbages:
        distance = ((goat.x - cabbage.x) ** 2 + (goat.y - cabbage.y) ** 2) ** 0.5
        if distance < min and cabbage.val > 0:
            min = distance
            nearest = cabbage
    return nearest