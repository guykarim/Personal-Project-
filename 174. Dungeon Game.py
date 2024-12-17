class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * (n + 1)
        dp[n-1] = 1
        
        for i in range(m-1, -1, -1):
            next_row = dp[:]
            for j in range(n-1, -1, -1):
                min_health_on_exit = min(next_row[j], dp[j+1])
                dp[j] = max(1, min_health_on_exit - dungeon[i][j])
        
        return dp[0]
