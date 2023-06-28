"""

===========================================================================
Game: Sudoku.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\b')


# Finds the empty positions of the board
def FindEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j

    return None


def Valid(bo, num, pos):
    # Checking the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def Solve(bo):
    find = FindEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if Valid(bo, i, (row, col)):
            bo[row][col] = i

            if Solve(bo):
                return True

            bo[row][col] = 0

    return False


# Prints the board
def PrintBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def main():
    Header()
    board = [[0, 0, 6,  0, 9, 0,  0, 4, 0],
             [0, 0, 0,  3, 7, 1,  0, 0, 8],
             [0, 3, 0,  0, 0, 0,  9, 0, 7],

             [4, 0, 0,  5, 8, 0,  6, 0, 0],
             [0, 0, 0,  0, 0, 0,  0, 0, 0],
             [0, 0, 3,  6, 0, 7,  0, 0, 5],

             [2, 0, 8,  0, 0, 0,  0, 3, 0],
             [5, 0, 0,  7, 3, 8,  0, 0, 0],
             [0, 1, 0,  0, 2, 0,  5, 0, 0]]
    print('\nExample Board:\n')
    PrintBoard(board)
    Solve(board)
    line()
    print('\nSolved Board:\n')
    PrintBoard(board)


main()
