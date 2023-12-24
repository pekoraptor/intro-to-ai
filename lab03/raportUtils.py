from minimax import alphabeta
from heuristic import connectFourHeuristic
from two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState
from two_player_games.player import Player
import random
import pandas as pd
import matplotlib.pyplot as plt


def botVsBot(d1, d2, games):
    wins1 = 0
    draws = 0
    wins2 = 0

    for _ in range(games):
        g = ConnectFour((7, 6), Player('1'), Player('2'))
        while not g.is_finished():
            g.make_move(alphabeta(g.state, d1, -float('inf'),
                        float('inf'), '1', connectFourHeuristic)[1])
            if not g.is_finished():
                g.make_move(alphabeta(g.state, d2, -float('inf'),
                                      float('inf'), '2', connectFourHeuristic)[1])

        winner = g.get_winner()
        if winner:
            if winner.char == '1':
                wins1 += 1
            else:
                wins2 += 1
        else:
            draws += 1

    return (wins1, draws, wins2)


def botVsRandom(d, games):
    winCount = 0
    drawCount = 0
    lossCount = 0

    for i in range(games):
        g = ConnectFour((7, 6), Player('1'), Player('2'))
        while not g.is_finished():
            g.make_move(ConnectFourMove(random.randrange(7)))
            if not g.is_finished():
                g.make_move(alphabeta(g.state, d, -float('inf'), +
                                      float('inf'), '2', connectFourHeuristic)[1])

        winner = g.get_winner()
        if winner:
            if winner.char == '2':
                winCount += 1
            else:
                lossCount += 1
        else:
            drawCount += 1

    return winCount, drawCount, lossCount


def compareVsRandom(depths: list, games: int):
    wins = []
    draws = []
    losses = []
    for d in depths:
        output = botVsRandom(d, games)
        wins.append(output[0])
        draws.append(output[1])
        losses.append(output[2])

    evenWins = 0
    evenDraws = 0
    evenLosses = 0
    oddWins = 0
    oddDraws = 0
    oddLosses = 0

    evenCount = 0

    i = 0
    for w, d, l in zip(wins, draws, losses):
        if depths[i] % 2 == 0:
            evenWins += w
            evenDraws += d
            evenLosses += l
            evenCount += 1
        else:
            oddWins += w
            oddDraws += d
            oddLosses += l
        i += 1

    wins.append(evenWins)
    draws.append(evenDraws)
    losses.append(evenLosses)
    wins.append(oddWins)
    draws.append(oddDraws)
    losses.append(oddLosses)

    winPercentages = [str(round((w / games)*100, 1))+'%' for w in wins[:-2]]
    winPercentages.append(str(round((wins[-2]*100)/(games*evenCount), 1))+'%')
    winPercentages.append(
        str(round((wins[-1]*100)/(games*(len(depths) - evenCount)), 1))+'%')

    data = {"Wins": wins,
            "Draws": draws,
            "Losses": losses,
            "Win%": winPercentages}
    indexes = [str(d) for d in depths]
    indexes.append('Even')
    indexes.append('Odd')

    df = pd.DataFrame(data, index=indexes)
    return df


def compareBotVsBot(depths1: list, depths2: list, games: int):
    wins1 = []
    draws = []
    wins2 = []

    for d1, d2 in zip(depths1, depths2):
        output1 = botVsBot(d1, d2, games)
        output2 = botVsBot(d2, d1, games)
        wins1.append(output1[0] + output2[2])
        draws.append(output1[1] + output2[1])
        wins2.append(output1[2] + output2[0])

    winPercentages = [str(round((w / (2*games))*100, 1))+'%' for w in wins1]

    data = {"VS": depths2, "Wins": wins1,
            "Draws": draws,
            "Losses": wins2,
            "Win%": winPercentages}

    df = pd.DataFrame(data, index=depths1)
    return df


def compareDepthsOnSingleGame(depths: list):
    colors = ['r', 'g', 'b', 'y']
    g = ConnectFour((7, 6), Player('1'), Player('2'))
    results = [[] for _ in range(len(depths))]

    while not g.is_finished():
        g.make_move(ConnectFourMove(random.randrange(7)))
        state = g.state
        if not g.is_finished():
            output = alphabeta(g.state, depths[0], -float('inf'), +
                               float('inf'), '2', connectFourHeuristic)
            g.make_move(output[1])
            results[0].append(output[0])
        for i, d in enumerate(depths[1:]):
            results[i + 1].append(alphabeta(state, d, -float('inf'), +
                                            float('inf'), '2', connectFourHeuristic)[0])

    plt.title('Values of moves found by alphabeta with each depth')
    plt.xlabel('Move')
    plt.ylabel('Value')
    for r, c, d in zip(results, colors, depths):
        plt.plot(r, c + 'o', markersize=2, label=f'Depth = {d}')
        plt.plot(r, c, linewidth=0.2)
    plt.legend()
    plt.show()
