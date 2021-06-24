import numpy as np

class Matrix:
    def __init__(self):
        self.rows, self.columns = 6, 7
        self.matrix = np.zeros([self.rows, self.columns])

    def add_Chip(self, player, col):

        try:
            for i in range(self.rows):
                if self.matrix[i][col] == 0:
                    self.matrix[i][col] = player

        except:
            print("not okey for player {}".format(player))

        finally:
            print("Did not work")

    def print_board(self):
        print(self.matrix)