from minimax import alphabeta
from heuristic import connectFourHeuristic
from two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState
from two_player_games.player import Player
import os
import math
import random


def testRandom(games, d):
    winCount = 0
    drawCount = 0
    lossCount = 0

    for i in range(games):
        print(i)
        g = ConnectFour((7, 6), Player('1'), Player('2'))
        while not g.is_finished():
            g.make_move(ConnectFourMove(random.randrange(7)))
            if not g.is_finished():
                g.make_move(alphabeta(g.state, d, -math.inf, +
                                      math.inf, '2', connectFourHeuristic)[1])

        if g.get_winner().char == '2':
            winCount += 1
        elif g.get_winner().char == '1':
            lossCount += 1
        else:
            drawCount += 1
    return winCount, drawCount, lossCount


def play():
    os.system('cls' if os.name == 'nt' else 'clear')
    g = ConnectFour((7, 6), Player('1'), Player('2'))
    while not g.is_finished():
        print(g.state)
        print(connectFourHeuristic(g.state, '2'))
        playerMove = int(input('Input your move:    '))
        g.make_move(ConnectFourMove(playerMove))
        if g.is_finished():
            break
        _, botMove = alphabeta(g.state, 5, -math.inf,
                               math.inf, '2', connectFourHeuristic)
        g.make_move(botMove)
    print(g.get_winner())


def soloPlay():
    os.system('cls' if os.name == 'nt' else 'clear')
    g = ConnectFour((7, 6), Player('1'), Player('2'))
    while not g.is_finished():
        print(g.state)
        print(connectFourHeuristic(g.state, '2'))
        playerMove = int(input('Input your move:    '))
        g.make_move(ConnectFourMove(playerMove))
        playerMove = int(input('Input your move:    '))
        if g.is_finished():
            break
        g.make_move(ConnectFourMove(playerMove))
    print(g.get_winner())


if __name__ == "__main__":
    print(testRandom(1000, 3))
    # play()
