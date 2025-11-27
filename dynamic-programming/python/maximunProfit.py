"""
Best Time to Buy and Sell Stock IV (LeetCode 188)

PATTERN: Dynamic Programming - 3D State Space
- At most k transactions allowed
- Track: day, transactions remaining, holding status

TIME COMPLEXITY: O(n * k) - n days, k transactions
SPACE COMPLEXITY: O(n * k) for the DP table

WHY THIS WORKS:
- State space: (day, transactions_left, holding_stock)
- At each state, choose the action that maximizes profit
- Use tabulation (bottom-up) for efficiency
"""


def max_profit(k: int, prices: list[int]) -> int:
    """
    Find max profit with at most k transactions.

    A transaction = 1 buy + 1 sell.

    Args:
        k: Maximum number of transactions allowed
        prices: Stock prices on each day

    Returns:
        Maximum profit achievable

    Visual:
        prices = [2, 4, 1], k = 2

        Possible transactions:
        - 0 transactions: profit = 0
        - 1 transaction: buy@2, sell@4 = 2 (best!)
        - 2 transactions: not possible to improve

        State: dp[i][t][h]
        - i: day (0 to n-1)
        - t: transactions remaining (0 to k)
        - h: holding stock (0 or 1)

        dp[i][t][0] = max profit at day i, t transactions left, NOT holding
        dp[i][t][1] = max profit at day i, t transactions left, HOLDING
    """
    n = len(prices)
    if n == 0 or k == 0:
        return 0

    # Optimization: if k >= n/2, it's equivalent to unlimited transactions
    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

    # dp[i][t][h]: max profit at position i, t transactions left, holding=h
    # We iterate backwards from the last day
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

    # Fill table from day n-1 backwards to day 0
    for i in range(n - 1, -1, -1):
        for t in range(1, k + 1):
            for holding in range(2):
                if holding == 0:
                    # NOT holding: can buy or skip
                    # Buy: pay prices[i], gain future profit with stock
                    # Skip: keep same state
                    dp[i][t][0] = max(
                        dp[i + 1][t][0],              # Skip (stay not holding)
                        -prices[i] + dp[i + 1][t][1]  # Buy (now holding)
                    )
                else:
                    # HOLDING: can sell or hold
                    # Sell: gain prices[i], use 1 transaction
                    # Hold: keep stock, same transactions
                    dp[i][t][1] = max(
                        dp[i + 1][t][1],              # Hold (stay holding)
                        prices[i] + dp[i + 1][t - 1][0]  # Sell (use 1 transaction)
                    )

    # Answer: start at day 0, k transactions, not holding
    return dp[0][k][0]


def max_profit_forward(k: int, prices: list[int]) -> int:
    """
    Alternative: Forward iteration approach.
    """
    n = len(prices)
    if n == 0 or k == 0:
        return 0

    if k >= n // 2:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

    # dp[t][0] = max profit with t transactions, not holding
    # dp[t][1] = max profit with t transactions, holding
    dp = [[0, float('-inf')] for _ in range(k + 1)]

    for price in prices:
        for t in range(k, 0, -1):
            # Update not holding (can sell from holding state)
            dp[t][0] = max(dp[t][0], dp[t][1] + price)
            # Update holding (can buy from not holding state of t-1 transactions)
            dp[t][1] = max(dp[t][1], dp[t - 1][0] - price)

    return dp[k][0]


# Test cases
if __name__ == "__main__":
    # Example 1: k=2, simple case
    print(max_profit(2, [2, 4, 1]))  # 2 (buy@2, sell@4)

    # Example 2: k=2, multiple transactions
    print(max_profit(2, [3, 2, 6, 5, 0, 3]))  # 7
    # Buy@2, sell@6 (+4), buy@0, sell@3 (+3) = 7

    # Example 3: k=1, same as problem 121
    print(max_profit(1, [7, 1, 5, 3, 6, 4]))  # 5 (buy@1, sell@6)

    # Forward approach
    print(max_profit_forward(2, [3, 2, 6, 5, 0, 3]))  # 7

    """
    STOCK PROBLEMS FAMILY:

    LeetCode 121: 1 transaction (simple DP)
    LeetCode 122: Unlimited transactions (greedy)
    LeetCode 123: At most 2 transactions (special case of 188)
    LeetCode 188: At most k transactions (this problem)
    LeetCode 309: Unlimited with cooldown (state machine)
    LeetCode 714: Unlimited with fee (2-state DP)

    KEY INSIGHT FOR k TRANSACTIONS:

    When k >= n/2, we can capture every upward price movement,
    making it equivalent to unlimited transactions (greedy solution).

    When k < n/2, we need full DP to track transaction count.
    """
