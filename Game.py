import random
from Board import Board


class Game:

    def __init__(self, player1, player2, mode):
        self.player1 = player1
        self.player2 = player2
        self.mode = mode
        self.board = Board()
        self.current_player = self.player1

    def start(self):

        while not self.board.is_over():
            pos = self.current_player.move(self.board)
            self.board.set_label(pos, self.current_player.getLabel())
            self.swap()
            if self.mode is "play":
                self.board.print()
        self.update()

    def swap(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def update(self):
        if self.mode == 'train':
            if random.random() <= 0.5:
                self.player1.update(self.board.get_winner())
            else:
                self.player2.update(-1*self.board.get_winner())
