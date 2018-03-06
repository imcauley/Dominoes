from card import Card

class Board:
    def __init__(self, size):
        self.onBoard = []
        self.set = self.create_set(size)
        self.size = size
        self.left = 0
        self.right = 0

    def print_board(self):
        for card in self.onBoard:
            card.print_card()

    def place_card(self,card,spot):
        if(spot == 0):
            if(self.onBoard == []):
                self.onBoard.append(card)
                self.left = card.left
                self.right = card.right
            else:
                return False
        if(spot == -1):
            if(card.right == self.left):
                self.onBoard = [card] + self.onBoard
                self.left = card.left
            else:
                return False
        if(spot == 1):
            if(card.left == self.right):
                self.onBoard = self.onBoard + [card]
                self.right = card.right
            else:
                return False

    def open_spots(self):
        spots = []
        spots.append(onBoard[0].left)
        spots.append(onBoard[-1].right)
        return spots

    def create_set(self,size):
        new_set = []
        if(size == -1):
            return new_set
        else:
            for n in range(0,size):
                new_set.append(Card((size-1),n))

            new_set = new_set + (self.create_set(size-1))
            return new_set
