class Board:

    def __init__(self):
        self.labels = [0]*9
        self.winner = 0

    def set_label(self, position, label):
        self.labels[position] = label

    def get_state(self):
        return self.labels

    def get_winner(self):
        return self.winner

    def is_over(self):
        rows = [sum(self.labels[i:i+3]) for i in range(3)]
        cols = [sum(self.labels[i:9:3]) for i in range(3)]
        diags = [sum(self.labels[0:9:4]), sum(self.labels[2:7:2])]
        cols.extend(diags)
        rows.extend(cols)
        return self.is_winner(rows)

    def is_winner(self, arr):
        if 3 in arr:
            self.winner = 1
            return True
        if -3 in arr:
            self.winner = -1
            return True
        if 0 not in self.labels:
            self.winner = 0
            return True
        return False

    def available_moves(self):
        return [i for i in range(9) if self.labels[i] == 0]

    def print(self):
        getMark = {1: "X", -1: "O", 0: " "}
        idx = [getMark.get(i) for i in self.labels]
        board = """
                     {} | {} | {}
                    -----------
                     {} | {} | {}
                    -----------
                     {} | {} | {}
                """.format(*idx)
        print(board)

