from game import Game
from player import Player
from ai_player import AI_Player

players = [Player(0), AI_Player(1), AI_Player(2), AI_Player(3)]
g = Game(7,players)
g.play_game()
