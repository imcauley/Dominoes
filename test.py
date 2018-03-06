from card import Card
from board import Board

board1 = Board(7)

board1.print_board()
board1.place_card(Card(6,6),0)
board1.place_card(Card(6,1),1)
board1.place_card(Card(2,1),1)
board1.place_card(Card(2,1),-1)
board1.place_card(Card(2,6),-1)
board1.print_board()
