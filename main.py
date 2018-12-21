from Game import Game
from RL_AI import RL_AI
from Player import Player
import numpy as np


def main():
    file_name = "TTT/policy.txt"
    print("Play with bot or train? (play/train)\n")

    if input() == "train":
        print("How many games for training?\n")
        train(file_name, int(input()))

    else:
        play(file_name)


def train(file_name, N):
    list = [ round(a) for a in np.linspace(0, N, 10, False)]
    print(list)
    filename = None
    for i in range(N):
        if i in list:
            print("{}%".format(str(list.index(i) * 10)))

        plX = RL_AI(1, filename, True)
        plO = RL_AI(-1, filename, True)
        game = Game(plX, plO, 'train')
        game.start()
        filename = file_name


def play(file_name):
    print("Do you want to start first? (yes/no)\n")
    if input() == 'yes':
        bot = RL_AI(-1, file_name)
        human = Player(1)
        game = Game(human, bot, 'play')
    else:
        bot = RL_AI(1, file_name)
        human = Player(-1)
        game = Game(bot, human, 'play')

    bot.playSerious()
    game.start()


if __name__ == "__main__":
    main()
