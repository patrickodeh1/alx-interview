#!/usr/bin/python3
"""
N Queens Problem Solver
Usage: nqueens N
"""

import sys


def print_usage_and_exit(message, status):
    """Prints an error message and exits the program."""
    print(message)
    sys.exit(status)


def is_safe(board, row, col, N):
    """Check if a queen can be placed on board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, col, N, results):
    """Recursive utility to solve the N Queens problem."""
    if col == N:
        solution = [[i, board[i].index(1)] for i in range(N)]
        results.append(solution)
        return
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, N, results)
            board[i][col] = 0


def solve_nqueens(N):
    """Solves the N Queens problem for a given N."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    results = []
    solve_nqueens_util(board, 0, N, results)
    return results


def main():
    """Main entry point for the program."""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)

    if N < 4:
        print_usage_and_exit("N must be at least 4", 1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
