import copy

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

board = [row[:] for row in grid]


def get_box_borders(row, col):
    start_row = -1
    start_col = -1

    if row < 3:
        start_row = 0
    elif row < 6:
        start_row = 3
    else:
        start_row = 6

    if col < 3:
        start_col = 0
    elif col < 6:
        start_col = 3
    else:
        start_col = 6

    return (start_row, start_col)


def is_safe(board, row, col, number):

    for i in range(9):
        if board[row][i] == number:
            return False

    for i in range(9):
        if board[i][col] == number:
            return False

    start_row, start_col = get_box_borders(row, col)

    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if board[i][j] == number:
                return False

    return True


def check_if_board_solved():
    board_solved = False
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (board_solved, i, j)

    return (True, 0, 0)


def solve_sudoku():
    board_solved, row, col = check_if_board_solved()
    if board_solved:
        return True

    for i in range(1, 10):
        if is_safe(grid, row, col, i):
            grid[row][col] = i
            if solve_sudoku():
                return True

            grid[row][col] = 0

    return False


def print_solved_boared(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end="")
            if j == 2 or j == 5:
                print(" ", end="")

        print("")
        if i == 2 or i == 5:
            print("")


def main():
    global grid
    while True:
        print_solved_boared(board)
        print("Enter row, col, number:")
        user_input = input()
        if not "," in user_input:
            print_solved_boared(board)
            return

        user_input = user_input.split(",")
        row = int(user_input[0])
        col = int(user_input[1])
        number = int(user_input[2])
        if not is_safe(grid, row, col, number):
            print(f"{number} is not save for this position!")
            continue

        grid[row][col] = number
        result = solve_sudoku()
        if not result:
            print(f"{number} is wrong for this position")
            grid[row][col] = 0
            continue

        board[row][col] = number
        grid = [row[:] for row in board]
        print(f"{number} is right for this position! Please continue...")
        if check_if_board_solved():
            print("Congrats, Board is Solved!!!")
            print()
            break

    print_solved_boared()


if __name__ == "__main__":
    main()
