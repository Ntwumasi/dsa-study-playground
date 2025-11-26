def maxProfit(prices, k):
    n = len(prices)
    if n == 0:
        return 0
    # once this is done we want to create a table to store
    # the values assigned, essentially the prices, the transactions
    # and weather or not we are holding.  
    # we need to build a 3d array to store the values
    
    dp = [[[0] * 2 for _ in range(n + 1)]for _ in range(k + 1)]

    # we just built the table to hold the values
    # next we will need to build the logic for calculating the profit made

    for i in range(n-1, -1, -1):
        for t in range(1, k + 1):
            for holding in range(2):
    # we need to get to the meat of the equation
    # which is the logic that will handle the subproblem
    # please note we are using tabulation, bottom up approach 
                if holding == 0:
                    # do some logic
                    # logic is if we arent holding get the max amount
                    # of when we arent holding versus when we buy 

                    dp[i][t][0] = max(
                        dp[i + 1][t][0],
                        -prices[i] + dp[i + 1][t][1]
                    )
                else:
                    # do some other logic
                    # logic is if we are holding get the max
                    # amount 
                    dp[i][t][1] = max(
                        dp[i + 1][t][1],
                        prices[i] + dp[i + 1][t - 1][0]
                    )
    return dp[0][k][0]

  