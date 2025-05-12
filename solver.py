"""
Reads a sudoku in from a file and then solves it using a recursive backtracker
"""
import sys

def read_file():
    """
    Read in the file, generating the list representation
    The list representation is a 2D Array of 9x9
    """
    board = []
    file_path = sys.argv[1]
    with open(file_path, encoding="utf-8") as file:
        for line in file.readlines():
            row = []
            rows = line.split("|")
            if len(rows) == 1:
                continue

            for cell in rows:
                for digit in cell:
                    digit = digit.strip()
                    if digit and digit != '.':
                        row.append(int(digit))
                    else:
                        row.append(0)

            board.append(row[:-1]) # Remove the new line that was added as a 0

    return board

def solve(board, row, col):
    """
    Recursive backtracking that solves the sudoku
    row and col represents the current row and col being filled
    """
    if col == 9:
        row += 1
        col = 0
    if row == 9: # If we reach the end of the board, then the solution is valid
        return board

    if board[row][col] != 0: # If prepopulated, continue search
        return solve(board, row, col + 1)

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            res = solve(board, row, col + 1)
            if res: # If a solution was found
                return res
            # If the previous attempt was unsuccessful, unset
            board[row][col] = 0

    return None # No solution was found at this branch

def is_valid(board, row, col, num):
    """
    Checks if the placement of the current number is valid. Validity is defined by:
        1. No duplicate num in the same row
        2. No duplicate num in the same col
        3. No duplicate num in the same cell
    """
    # Check if the num exists in the row / col
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if the num exists in the current cell
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def print_board(board):
    for i in range(9):
        if i != 0 and i % 3 == 0:
            print("-" * 11)

        for j in range(9):
            if j != 0 and j % 3 == 0:
                print("|", end="")
            print(board[i][j], end="")
        print()

    print()

def main():
    """
    Main progarm skeleton
    """
    board = read_file()

    solved = solve(board, 0, 0)

    if solved:
        print("Solved board:")
        print_board(solved)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
