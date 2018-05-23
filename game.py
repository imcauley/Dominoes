from card import Card
from board import Board
from player import Player

import random

class Game:
    def __init__(self,size,players,output=True):
        self.board = Board(size)
        self.set = self.create_set(size)
        random.shuffle(self.set)

        self.num_pieces = ((size) * (size + 1)) // 2

        self.players = players
        self.create_players()
        self.turn = 0

        self.output = output


    def play_game(self):
        prev_length = -1
        while(True):
            winner = self.winner()
            if(winner == None):
                self.next_turn()

                if self.turn % 4 == 0:
                    length = len(self.board.onBoard)
                    if length == prev_length:
                        return None
                    else:
                        prev_length = length

            else:
                return winner



    def winner(self):
        for number, p in enumerate(self.players):
            if len(p.pieces) == 0:
                return number

        return None

    def next_turn(self):
        player_num = self.turn % 4
        player = self.players[player_num]


        if self.output:
            print("Turn: ", self.turn)
            self.board.print_board()
            player.print_options()


        piece, position = player.get_piece(self.board)

        if piece != None:
            if not self.board.place_card(piece, position):
                player.pieces.append(piece)

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
