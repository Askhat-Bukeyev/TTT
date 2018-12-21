class Player:
    label = 1

    def __init__(self, lb=1):
        self.label = lb

    def move(self, board):
        pos = input().split(" ")
        return int(pos[0])*3 + int(pos[1])

    def getLabel(self):
        return self.label

    def update(self):
        pass
