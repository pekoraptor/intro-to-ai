# from two_player_games.games.connect_four import ConnectFour, ConnectFourMove, ConnectFourState
import math
import random
import copy


# def minimax(node, depth, maximizingPlayer, heuristic):
#     if depth == 0 or node.is_finished():
#         return heuristic(node, maximizingPlayer), None

#     bestMoves = []

#     if node.get_current_player().char == maximizingPlayer:
#         value = -math.inf
#         chosenMove = None
#         for move in node.get_moves():
#             newNode = copy.deepcopy(node)
#             newNode.make_move(move)
#             newVal, _ = minimax(newNode, depth - 1,
#                                 maximizingPlayer, heuristic)
#             if newVal > value:
#                 value = newVal
#                 bestMoves = [move]
#             elif newVal == value:
#                 bestMoves.append(move)
#         return value, random.choice(bestMoves)

#     else:
#         value = +math.inf
#         chosenMove = None
#         for move in node.get_moves():
#             newNode = copy.deepcopy(node)
#             newNode.make_move(move)
#             newVal, _ = minimax(newNode, depth - 1,
#                                 maximizingPlayer, heuristic)
#             if newVal < value:
#                 value = newVal
#                 bestMoves = [move]
#             elif newVal == value:
#                 bestMoves.append(move)
#         return value, random.choice(bestMoves)


def alphabeta(node, depth, a, b, maximizingPlayer, heuristic):
    if depth == 0 or node.is_finished():
        return heuristic(node, maximizingPlayer), None

    bestMoves = [None]

    if node.get_current_player().char == maximizingPlayer:
        value = -math.inf
        for move in node.get_moves():
            newNode = copy.deepcopy(node)
            newNode = newNode.make_move(move)
            newVal, _ = alphabeta(newNode, depth - 1, a, b,
                                  maximizingPlayer, heuristic)
            if newVal > value:
                value = newVal
                bestMoves = [move]
                a = max(a, newVal)
                if value >= b:
                    break
            elif newVal == value:
                bestMoves.append(move)
        return value, random.choice(bestMoves)

    else:
        value = +math.inf
        for move in node.get_moves():
            newNode = copy.deepcopy(node)
            newNode.make_move(move)
            newVal, _ = alphabeta(newNode, depth - 1, a, b,
                                  maximizingPlayer, heuristic)
            if newVal < value:
                value = newVal
                bestMoves = [move]
                b = min(b, value)
                if value <= a:
                    break
            elif newVal == value:
                bestMoves.append(move)
        return value, random.choice(bestMoves)
