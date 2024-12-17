class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # If k >= n // 2, unlimited transactions allowed
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))

        # Optimized space DP
        dp = [0] * n

        for t in range(1, k + 1):
            maxDiff = -prices[0]
            prev_dp = dp[:]
            for d in range(1, n):
                dp[d] = max(dp[d-1], prices[d] + maxDiff)
                maxDiff = max(maxDiff, prev_dp[d] - prices[d])

        return dp[-1]
