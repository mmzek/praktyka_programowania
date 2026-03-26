import time
import random

def count_neighbours(board):
    rows = len(board)
    cols = len(board[0])

    neighbours = [[0 for _ in range(cols)] for _ in range(rows)]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc]:
                        count += 1

            neighbours[r][c] = count

    return neighbours

def determine_status(nb, board):
    rows = len(board)
    cols = len(board[0])

    for r in range(rows):
        for c in range(cols):
            if not board[r][c] and nb[r][c] == 3:
                board[r][c] = True
            if board[r][c]:
                if nb[r][c] == 2 or nb[r][c] == 3:
                    continue
                elif nb[r][c] < 2 or nb[r][c] > 3:
                    board[r][c] = False

def print_board(board):
    for row in board:
        line = " ".join("O" if cell else "." for cell in row)
        print(line)

if __name__ == '__main__':
    rows = 10
    cols = 10

    board = [[random.choice([True, False]) for _ in range(cols)] for _ in range(rows)]

    for i in range(100):
        print("Iteracja " + str(i) + "\n")
        print_board(board)
        nb = count_neighbours(board)
        determine_status(nb, board)
        time.sleep(1.0)