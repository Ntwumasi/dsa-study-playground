def costToClimbStairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]

# Example input
cost = [10, 15, 20]

# Print the minimum cost to reach the top
print(costToClimbStairs(cost))