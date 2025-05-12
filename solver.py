"""
Reads a sudoku in from a file and then solves it using a recursive backtracker
"""
import sys
def main():
    """
    Main progarm skeleton
    """
    # Read in the file
    file_path = sys.argv[1]
    with open(file_path, encoding="utf-8") as file:
        for line in file.readlines():
            print(line)

    print("Hello World!")

if __name__ == "__main__":
    main()
