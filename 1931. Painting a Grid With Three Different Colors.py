'''
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''
class Solution:
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7
        
        # Generate all valid masks for a row of length n
        masks = []
        def generate_masks(mask, pos):
            if pos == n:
                masks.append(mask)
                return
            for color in range(3):  # 0 for red, 1 for green, 2 for blue
                if pos == 0 or ((mask >> (2 * (pos - 1))) & 3) != color:
                    generate_masks(mask | (color << (2 * pos)), pos + 1)
        
        generate_masks(0, 0)
        
        # Initialize dp array
        dp = [[0] * len(masks) for _ in range(m)]
        
        # Base case: first row
        for j in range(len(masks)):
            dp[0][j] = 1
        
        # Fill dp array
        for i in range(1, m):
            for j in range(len(masks)):
                for k in range(len(masks)):
                    if not self.has_conflict(masks[j], masks[k], n):
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
        
        # Sum up all dp[m-1][j] for valid masks j
        result = sum(dp[m-1][j] for j in range(len(masks))) % MOD
        
        return result
    
    def has_conflict(self, mask1, mask2, n):
        for i in range(n):
            color1 = (mask1 >> (2 * i)) & 3
            color2 = (mask2 >> (2 * i)) & 3
            if color1 == color2:
                return True
        return False
