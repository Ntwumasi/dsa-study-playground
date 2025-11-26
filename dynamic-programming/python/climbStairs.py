def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)  # dp[i] represents the number of ways to reach step i
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]