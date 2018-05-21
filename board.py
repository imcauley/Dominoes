from card import Card

class Board:
    def __init__(self, size):
        self.onBoard = []
        self.size = size
        self.left = 0
        self.right = 0

    def print_board(self):
        print("Board: ")

        [print("=", end='') for _ in range(len(self.onBoard)*5)]
        print("")

        for card in self.onBoard:
            card.print_card_for_board()

        print('')

        [print("=", end='') for _ in range(len(self.onBoard)*5)]
        print("")

    def place_card(self,card,spot):
        if self.onBoard == []:
            self.onBoard.append(card)
            self.left = card.left
            self.right = card.right
            return True

        elif(spot == -1):
            if(card.right == self.left):
                self.onBoard = [card] + self.onBoard
                self.left = card.left
                return True

        elif(spot == 1):
            if(card.left == self.right):
                self.onBoard = self.onBoard + [card]
                self.right = card.right
                return True

        return False

    def open_spots(self):
        spots = []
        spots.append(onBoard[0].left)
        spots.append(onBoard[-1].right)
        return spots
