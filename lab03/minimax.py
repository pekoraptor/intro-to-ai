from two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState
import math
import random
import copy


def addValue(start, final, isMaximizingPlayer):
    if (final - start) > 1:
        if isMaximizingPlayer:
            return (final - start)*10
        else:
            return - (final - start)*10


def connectFourHeuristic(node, maximizingPlayer):
    winner = node.get_winner()
    if winner:
        if winner == maximizingPlayer:
            return math.inf
        else:
            return -math.inf

    columns = len(node.fields)
    rows = len(node.fields[0])

    value = 0
    # check verticals
    for column_id in range(columns):
        player = node.fields[column_id][0]
        start = 0
        final = len(node.fields)
        for row_id in range(rows):
            if player is None:
                final = row_id
                break
            if node.fields[column_id][row_id] != player:
                start = row_id
                player = node.fields[column_id][row_id]
        value += addValue(start, final, (player == maximizingPlayer))

    # check horizontals
    for row_id in range(rows):
        player = node.fields[0][row_id]
        start = 0
        final = len(node.fields[0])
        for column_id in range(columns):
            if player is None:
                value += addValue(start, row_id, (player == maximizingPlayer))
                start = row_id

            elif node.fields[column_id][row_id] != player:
                start = column_id
                player = node.fields[column_id][row_id]
        value += addValue(start, final, (player == maximizingPlayer))


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
