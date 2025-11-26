def bestTimeToSell(prices):
    n = len(prices)
    if n == 0:
        return 0

    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        # Track the minimum price up to day i
        min_price = min(min_price, prices[i])
        # dp[i] stores the max profit if we sell on day i
        dp[i] = max(dp[i - 1], prices[i] - min_price)

    return dp[-1]