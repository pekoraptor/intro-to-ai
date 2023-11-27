from minimax import minimax, alphabeta
from heuristic import connectFourHeuristic
from two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState
from two_player_games.player import Player
import os
import math

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    g = ConnectFour((7, 6), Player('1'), Player('2'))
    # player 2 = bot
    while not g.is_finished():
        print(g.state)
        print(connectFourHeuristic(g.state, '2'))
        playerMove = int(input('Input your move:    '))
        g.make_move(ConnectFourMove(playerMove))
        if g.is_finished():
            break
        _, botMove = alphabeta(g.state, 2, -math.inf, +
                               math.inf, True, connectFourHeuristic)
        # _, botMove = minimax(g.state, 3, '2', connectFourHeuristic)
        g.make_move(botMove)
        # os.system('cls' if os.name == 'nt' else 'clear')
    print(g.get_winner())
