def check_winner(desk):
    n = len(desk)
    k = len(desk[0])

    for i in range(n):
        for j in range(n - k + 1):
            symbol = desk[i][j]
            if symbol == '_':
                continue
            if not all(desk[i][j + l] == symbol for l in range(k)):
                continue
            return symbol

    for i in range(n - k + 1):
        for j in range(n):
            symbol = desk[i][j]
            if symbol == '_':
                continue
            if not all(desk[i + l][j] == symbol for l in range(k)):
                continue
            return symbol

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            symbol = desk[i][j]
            if symbol == '_':
                continue
            if not all(desk[i + l][j + l] == symbol for l in range(k)):
                continue
            return symbol

    for i in range(n - k + 1):
        for j in range(k - 1, n):
            symbol = desk[i][j]
            if symbol == '_':
                continue
            if not all(desk[i + l][j - l] == symbol for l in range(k)):
                continue
            return symbol

    return "Ничья"


a = input()
board = [list(a)]

for i in range(len(a)-1):
    row = input()
    board.append(list(row))

winner = check_winner(board)

print(winner)