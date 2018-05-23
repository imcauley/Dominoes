from player import Player
import random

class AI_Player(Player):
    def get_piece(self, board):
        flip = 'n'

        for index, piece in enumerate(self.pieces):
            if(piece.left == board.right):
                pos = 1
                break
            elif(piece.right == board.left):
                pos = -1
                break
            elif(piece.right == board.right):
                pos = 1
                flip = 'f'
                break
            elif(piece.left == board.left):
                pos = -1
                flip = 'f'
                break
        else:
            return None,None

        piece = self.pieces.pop(int(index))


        if flip == 'f':
            piece.rotate()

        return piece, pos
