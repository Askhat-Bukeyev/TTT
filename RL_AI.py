import random
import numpy as np


class RL_AI:

    def __init__(self, mark=0, file_name=None, learn=False, alpha=0.2, gamma=0.9, epsilon=0.33):
        self.label = mark
        self.policy = {}
        self.learn = learn
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.history = []
        if file_name is not None:
            self.loadPolicy(file_name)

    def playSerious(self):
        print("Serious")
        self.epsilon = 0

    def getLabel(self):
        return self.label

    def move(self, board):

        state = board.get_state()
        available_moves = board.available_moves()
        valueList = [self.getValue(state, a) for a in available_moves]

        if random.random() < self.epsilon:
            move = random.choice(available_moves)
        else:
            greedy_moves = [i for i, val in enumerate(valueList) if val == max(valueList)]
            idx = random.choice(greedy_moves)
            move = available_moves[idx]

        self.history.append((tuple(state), move))
        return move

    def update(self, reward):
        if self.learn:
            for move in self.history:
                self.policy[move] = self.policy.get(move) + self.alpha * reward
            self.savePolicy()

    def getValue(self, state, action):
        if self.policy.get((tuple(state), action)) is None:
            self.policy[(tuple(state), action)] = 1.0
        return self.policy.get((tuple(state), action))

    def getPolicy(self):
        return self.policy

    def savePolicy(self):
        file = open("TTT/policy.txt", "w")
        for key in self.policy.keys():
            msg = [" ".join([str(i) for i in key[0]]), str(key[1]), str(self.policy.get(key))]
            file.write(",".join(msg))
            file.write("\n")

    def loadPolicy(self, file_name):
        with open(file_name, "r") as file:
            data = file.read().splitlines()

        for item in data:
            msg = item.split(",")
            state = [int(i) for i in msg[0].split(" ")]
            action = int(msg[1])
            value = float(msg[2])
            self.policy[(tuple(state), action)] = value
