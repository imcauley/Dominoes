from player import Player
import random

class AI_Player(Player):
    def get_piece(self, board):
        sides = [1,-1]
        flips = ['f','n']

        index = random.choice(range(len(self.pieces)))
        pos = random.choice(sides)
        flip = random.choice(flips)

        piece = self.pieces.pop(int(index))

        if flip == 'f':
            piece.rotate()

        return piece, pos
