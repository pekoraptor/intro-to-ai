import math


def addValue(start, final, isMaximizingPlayer):
    if abs(final - start) > 1:
        if isMaximizingPlayer:
            return abs(final - start)*10
        else:
            return - abs(final - start)*10


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
                start = column_id

            elif node.fields[column_id][row_id] != player:
                start = column_id
                player = node.fields[column_id][row_id]

        value += addValue(start, final, (player == maximizingPlayer))

    # check diagonals
    # from lower left (lower half)
    for column_id in range(columns):
        player = node.fields[column_id][0]
        start = 0
        final = min(columns - column_id, rows)
        for i in range(min(columns - column_id, rows)):
            if player is None:
                value += addValue(start, i, (player == maximizingPlayer))
                start = i

            if node.fields[column_id + i][i] != player:
                start = i
                player = node.fields[column_id + i][i]

        value += addValue(start, final, (player == maximizingPlayer))

    # upper half
    for row_id in range(rows)[1:]:
        player = node.fields[row_id][0]
        if player is None:
            break
        start = 0
        final = min(rows - row_id, columns)
        for i in range(min(rows - row_id, columns)):
            if player is None:
                value += addValue(start, i, (player == maximizingPlayer))
                start = i

            if node.fields[i][row_id + i] != player:
                start = i
                player = node.fields[i][row_id + i]

        value += addValue(start, final, (player == maximizingPlayer))

    # from lower right (lower half)
    for column_id in range(columns)[::-1]:
        player = node.fields[column_id][-1]
        start = 0
        final = min(column_id, rows)
        for i in range(min(column_id, rows)):
            if player is None:
                value += addValue(start, i, (player == maximizingPlayer))
                start = i

            if node.fields[column_id - i][i] != player:
                start = i
                player = node.fields[column_id - i][i]

        value += addValue(start, final, (player == maximizingPlayer))

    # upper half
    for row_id in range(rows)[1:]:
        player = node.fields[row_id][0]
        if player is None:
            break
        start = 0
        final = min(rows - row_id, columns)
        for i in range(min(rows - row_id, columns)):
            if player is None:
                value += addValue(start, i, (player == maximizingPlayer))
                start = i

            if node.fields[columns - i][row_id + i] != player:
                start = i
                player = node.fields[columns - i][row_id + i]

        value += addValue(start, final, (player == maximizingPlayer))
