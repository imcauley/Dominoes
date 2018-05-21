import random

class Player:
    def __init__(self, position):
        self.position = position
        self.pieces = []

    def add_pieces(self, set):
        self.pieces = set

    def print_options(self):
        print("Player, " + str(self.position) + "'s turn")
        print("Your Cards: ")

        count = 0
        for p in self.pieces:
            print(str(count) + ": ", end='')
            count += 1
            p.print_card()

    def get_piece(self, board):
        index, side, flip = self.user_input()

        if index == None:
            return None, None

        piece = self.pieces.pop(int(index))

        if flip == 'f':
            piece.rotate()

        if side == 'r':
            pos = 1
        else:
            pos = -1

        return piece, pos

    def user_input(self):
        string = input("Piece: ")
        if string  == "":
            return None, None, None
        else:
            string = list(string)

            index = string[0]
            side = string[1]
            flip = string[2]

            return index, side, flip
