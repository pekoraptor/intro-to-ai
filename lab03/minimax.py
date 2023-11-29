import random
import copy


def alphabeta(node, depth, a, b, maximizingPlayer, heuristic):
    if depth == 0 or node.is_finished() or len(node.get_moves()) == 0:
        return heuristic(node, maximizingPlayer), None

    bestMoves = []

    if node.get_current_player().char == maximizingPlayer:
        value = -float('inf')
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
        value = float('inf')
        for move in node.get_moves():
            newNode = copy.deepcopy(node)
            newNode = newNode.make_move(move)
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
