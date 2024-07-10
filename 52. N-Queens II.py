'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

 

Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 9'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_valid(board, row, col):
            # Check if the column has a queen
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            # Check the 45-degree diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check the 135-degree diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        def solve(board, row):
            if row == n:
                self.count += 1
                return
            
            for col in range(n):
                if is_valid(board, row, col):
                    board[row][col] = 'Q'
                    solve(board, row + 1)
                    board[row][col] = '.'
        
        self.count = 0
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(board, 0)
        return self.count

solver = Solution()
print(solver.totalNQueens(4))  # Output: 2
print(solver.totalNQueens(1))  # Output: 1
