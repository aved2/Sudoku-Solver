sudoku = [
    [0,0,0,8,0,0,4,2,0],
    [5,0,0,6,7,0,0,0,0],
    [0,0,0,0,0,9,0,0,5],
    [7,4,0,1,0,0,0,0,0],
    [0,0,9,0,3,0,7,0,0],
    [0,0,0,0,0,7,0,4,8],
    [8,0,0,4,0,0,0,0,0],
    [0,0,0,0,9,8,0,0,3],
    [0,9,5,0,0,3,0,0,0]
]

def print_board(board):
    for i, val in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j, val in enumerate(board[0]):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def open_space(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)  # row, col

    return None


def valid(board, num, pos):

    
    # Check Row
    for i, val in enumerate(board[0]):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i, val in enumerate(board):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check Square
    square_x = pos[1] // 3
    square_y = pos[0] // 3

    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x * 3, square_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def solve(board):
    find = open_space(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


print_board(sudoku)
solve(sudoku)
print("")
print("Solved:")
print_board(sudoku)
