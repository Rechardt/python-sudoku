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

def main():
    """
    Main progarm skeleton
    """
    board = read_file()

    # Print the 1st index in the second cell
    print(board[0][0])


if __name__ == "__main__":
    main()
