from card import Card
from board import Board
from player import Player

import random

class Game:
    def __init__(self,size,players):
        self.board = Board(size)
        self.set = self.create_set(size)
        random.shuffle(self.set)

        self.num_pieces = ((size) * (size + 1)) // 2

        print(len(self.set))
        print(self.num_pieces)
        self.players = players
        self.create_players()
        self.turn = 0


    def play_game(self):
        while(self.no_win()):
            self.next_turn()

    def no_win(self):
        for p in self.players:
            if p.pieces == []:
                return False

        return True

    def next_turn(self):
        player_num = self.turn % 4

        print("Turn: ", self.turn)
        self.board.print_board()

        player = self.players[player_num]
        player.print_options()

        piece, position = player.get_piece(self.board)

        if piece != None:
            if not self.board.place_card(piece, position):
                player.pieces.append(piece)
                print("\n test \n")

        self.turn += 1


    def create_players(self):
        NUM_PLAYERS = 4

        for p in self.players:
            pieces = []

            for _ in range(self.num_pieces // 4):
                pieces.append(self.set.pop())

            p.add_pieces(pieces)


    def create_set(self,size):
        new_set = []
        if(size == -1):
            return new_set
        else:
            for n in range(0,size):
                new_set.append(Card((size-1),n))

            new_set = new_set + (self.create_set(size-1))
            return new_set
