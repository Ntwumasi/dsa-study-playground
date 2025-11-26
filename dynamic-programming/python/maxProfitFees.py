def maxProfit(prices, fee):
    n = len(prices)
    if n == 0:
        return 0

    dp = [[0] * 2 for _ in range(n)]

    # Base case
    dp[0][0] = 0              # Not holding stock
    dp[0][1] = -prices[0]     # Bought on day 0

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

    return dp[n - 1][0]  # On last day, max profit is with no stock held