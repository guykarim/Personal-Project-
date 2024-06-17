/*
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
*/

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check if the number is in the same row
            for i in range(9):
                if board[row][i] == num:
                    return False

            # Check if the number is in the same column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check if the number is in the same 3x3 sub-box
            box_row_start = (row // 3) * 3
            box_col_start = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[box_row_start + i][box_col_start + j] == num:
                        return False

            return True

        def find_empty(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)
            return None

        def backtrack(board):
            empty_cell = find_empty(board)
            if not empty_cell:
                return True  # Puzzle solved
            row, col = empty_cell

            for num in '123456789':
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    if backtrack(board):
                        return True
                    board[row][col] = '.'  # Undo move

            return False

        backtrack(board)
