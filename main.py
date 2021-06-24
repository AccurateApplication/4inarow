from Matrix import Matrix

running = True

class Main:
    def __init__(self):
        test = 0
        self.matrix = Matrix()

    def print_board(self):
        self.matrix.print_board()


if __name__ == '__main__':
    while running:
        print(Main().print_board())
        # Main().
        running = False
