import math


def addValue(start, final, isMaximizingPlayer):
    length = abs(final - start)
    if length > 1:
        value = 1000 if length == 2 else 10000
        if length == 4:
            value = math.inf
        if isMaximizingPlayer:
            return value
        else:
            return - value
    return 0


def connectFourHeuristic(node, maximizingPlayer):
    winner = node.get_winner()
    if winner is not None:
        if winner.char == maximizingPlayer:
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
        final = len(node.fields[0])
        for row_id in range(rows):
            if node.fields[column_id][row_id] is None:
                final = row_id
                break
            elif node.fields[column_id][row_id] != player:
                start = row_id
                player = node.fields[column_id][row_id]

        if player is not None and final != rows and rows - start >= 4:
            value += addValue(start, final, player.char == maximizingPlayer)

    # check horizontals
    for row_id in range(rows):
        player = node.fields[0][row_id]
        start = 0
        final = len(node.fields)
        for column_id in range(columns):
            if node.fields[column_id][row_id] is None:
                if player is not None:
                    value += addValue(start, column_id,
                                      player.char == maximizingPlayer)
                start = column_id

            elif node.fields[column_id][row_id] != player:
                start = column_id
                player = node.fields[column_id][row_id]

        if player is not None:
            value += addValue(start, final, player.char == maximizingPlayer)

    # check diagonals
    # from lower left (lower half)
    for column_id in range(columns):
        player = node.fields[column_id][0]
        start = 0
        final = min(columns - column_id, rows)
        for i in range(min(columns - column_id, rows)):
            if node.fields[column_id + i][i] is None:
                if player is not None:
                    value += addValue(start, i, player.char ==
                                      maximizingPlayer)
                start = i

            elif node.fields[column_id + i][i] != player:
                start = i
                player = node.fields[column_id + i][i]

        if player is not None:
            value += addValue(start, final, player.char == maximizingPlayer)

    # upper half
    for row_id in range(rows)[1:]:
        player = node.fields[row_id][0]
        if player is None:
            break
        start = 0
        final = min(rows - row_id, columns)
        for i in range(min(rows - row_id, columns)):
            if node.fields[i][row_id + i] is None:
                if player is not None:
                    value += addValue(start, i, player.char ==
                                      maximizingPlayer)
                start = i

            elif node.fields[i][row_id + i] != player:
                start = i
                player = node.fields[i][row_id + i]

        if player is not None:
            value += addValue(start, final, player.char == maximizingPlayer)

    # from lower right (lower half)
    for column_id in range(columns)[::-1]:
        player = node.fields[column_id][-1]
        start = 0
        final = min(column_id, rows)
        for i in range(min(column_id, rows)):
            if node.fields[column_id - i][i] is None:
                if player is not None:
                    value += addValue(start, i, player.char ==
                                      maximizingPlayer)
                start = i

            elif node.fields[column_id - i][i] != player:
                start = i
                player = node.fields[column_id - i][i]

        if player is not None:
            value += addValue(start, final, player.char == maximizingPlayer)

    # upper half
    for row_id in range(rows)[1:]:
        player = node.fields[row_id][0]
        if player is None:
            break
        start = 0
        final = min(rows - row_id, columns)
        for i in range(min(rows - row_id, columns)):
            if node.fields[columns - 1 - i][row_id + i] is None:
                if player is not None:
                    value += addValue(start, i, player.char ==
                                      maximizingPlayer)
                start = i

            elif node.fields[columns - 1 - i][row_id + i] != player:
                start = i
                player = node.fields[columns - 1 - i][row_id + i]
        if player is not None:
            value += addValue(start, final, player.char == maximizingPlayer)

    return value
