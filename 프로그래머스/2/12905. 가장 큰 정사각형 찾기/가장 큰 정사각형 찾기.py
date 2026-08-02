def solution(board):
    rows = len(board)
    cols = len(board[0])

    max_size = 0

    for r in range(rows):
        max_size = max(max_size, max(board[r]))

    for r in range(1, rows):
        for c in range(1, cols):

            if board[r][c] == 1:
                board[r][c] = min(board[r - 1][c], board[r][c - 1], board[r - 1][c - 1]) + 1

                max_size = max(max_size, board[r][c])

    return max_size ** 2