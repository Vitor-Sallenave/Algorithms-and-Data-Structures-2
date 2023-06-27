"""

===========================================================================
Problem: Given N Queens, how many ways we can set them in a chess board
(NxN) following the constraint below:

- Queens can not attack each other
(None of the queens can be in the same column, diagonal or row)
===========================================================================

"""


def CreateBoard(n):
    return [[0] * n for _ in range(n)]


def VerifyRowCol(board, N, row, col):
    # Verify if there is already a queen in the row/column
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    return True


def VerifyMainDiagonal(board, N, row, col):
    # Verifying the main diagonal positions above (row, col)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Verifying the main diagonal positions below (row, col)
    for i, j in zip(range(row, N), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def VerifySecondaryDiagonal(board, N, row, col):
    # Verifying the secondary diagonal positions above (row, col)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    # Verifying the secondary diagonal positions below (row, col)
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def VerifyDiagonals(board, N, row, col):
    return VerifySecondaryDiagonal(board, N, row, col) and VerifyMainDiagonal(board, N, row, col)


def VerifyMovement(board, N, row, col):
    return VerifyRowCol(board, N, row, col) and VerifyDiagonals(board, N, row, col)


def Solve(board, N, col):
    if col == N:
        print('\b')
        for row in board:
            print(' '.join(map(str, row)))
        return True

    # Going through the chess board
    for row in range(N):
        if VerifyMovement(board, N, row, col):
            # Set the queen (row, col)
            board[row][col] = 1

            # Next column
            if Solve(board, N, col + 1):
                return True
            else:
                # if there is no solution, removes the queen from the position (row, col)
                board[row][col] = 0

    return False


def main():
    # Creating the default chess board (8x8)
    N = 8
    board = CreateBoard(N)
    print('\nCHESS BOARD')
    answer = Solve(board, N, 0)
    print(f'\n{answer}\n')


main()
