from two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState
import math
import random
import copy


def minimax(node, depth, maximizingPlayer, heuristic):
    if depth == 0 or node.is_finished():
        return heuristic(node), None

    bestMoves = []

    if node.get_current_player() == maximizingPlayer:
        value = -math.inf
        chosenMove = None
        for move in node.get_moves():
            newNode = copy.deepcopy(node)
            newNode.make_move(move)
            newVal, = minimax(newNode, depth - 1, maximizingPlayer, heuristic)
            if newVal > value:
                value = newVal
                bestMoves = [move]
            elif newVal == value:
                bestMoves.append(move)
        return value, random.choice(bestMoves)

    else:
        value = +math.inf
        chosenMove = None
        for move in node.get_moves():
            newNode = copy.deepcopy(node)
            newNode.make_move(move)
            newVal, = minimax(newNode, depth - 1, maximizingPlayer, heuristic)
            if newVal < value:
                value = newVal
                bestMoves = [move]
            elif newVal == value:
                bestMoves.append(move)
        return value, random.choice(bestMoves)


g = ConnectFour()
print(g.state.fields)
