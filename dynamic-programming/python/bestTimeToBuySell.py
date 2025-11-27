"""
Best Time to Buy and Sell Stock (LeetCode 121)

PATTERN: Dynamic Programming - Single Transaction
- Buy once, sell once (must buy before selling)
- Find maximum profit possible

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(1) - only tracking min price and max profit

WHY THIS WORKS:
- For each day, the max profit if we sell today = price[i] - min_price_so_far
- We track the minimum price seen and maximum profit possible
- This is a simplified DP where we only need one variable for state
"""


def max_profit(prices: list[int]) -> int:
    """
    Find maximum profit from a single buy-sell transaction.

    Args:
        prices: Stock prices on each day

    Returns:
        Maximum profit (0 if no profit possible)

    Visual:
        prices = [7, 1, 5, 3, 6, 4]

        Day 0: price=7, min=7, profit=0 (can't sell yet)
        Day 1: price=1, min=1, profit=0 (price dropped)
        Day 2: price=5, min=1, profit=5-1=4
        Day 3: price=3, min=1, profit=3-1=2 (profit dropped, keep 4)
        Day 4: price=6, min=1, profit=6-1=5 ← new max!
        Day 5: price=4, min=1, profit=4-1=3 (keep 5)

        Answer: 5 (buy at 1, sell at 6)
    """
    if not prices:
        return 0

    min_price = prices[0]  # Minimum price seen so far
    max_profit_val = 0     # Maximum profit possible

    for i in range(1, len(prices)):
        # Update minimum price if we found a lower one
        min_price = min(min_price, prices[i])

        # Calculate profit if we sell today
        profit_today = prices[i] - min_price

        # Update max profit
        max_profit_val = max(max_profit_val, profit_today)

    return max_profit_val


def max_profit_dp(prices: list[int]) -> int:
    """
    Explicit DP approach (same logic, more memory).

    dp[i] = max profit achievable considering days 0 to i
    """
    if not prices:
        return 0

    n = len(prices)
    dp = [0] * n
    min_price = prices[0]

    for i in range(1, n):
        # Track minimum price up to day i
        min_price = min(min_price, prices[i])

        # Max profit: either keep previous max OR sell today
        dp[i] = max(dp[i - 1], prices[i] - min_price)

    return dp[-1]


# Test cases
if __name__ == "__main__":
    # Example 1: Profit possible
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Prices {prices1}: profit = {max_profit(prices1)}")  # 5

    # Example 2: No profit (prices always decreasing)
    prices2 = [7, 6, 4, 3, 1]
    print(f"Prices {prices2}: profit = {max_profit(prices2)}")  # 0

    # Example 3: Buy on first day, sell on last
    prices3 = [1, 2, 3, 4, 5]
    print(f"Prices {prices3}: profit = {max_profit(prices3)}")  # 4

    # Example 4: Single day
    prices4 = [5]
    print(f"Prices {prices4}: profit = {max_profit(prices4)}")  # 0

    """
    KEY INSIGHT:

    For any selling day i, the best buying day is:
    - The day with MINIMUM price BEFORE day i

    So for each day, we only need to track:
    1. The minimum price seen so far
    2. The maximum profit seen so far

    This reduces the problem from O(n²) brute force to O(n).

    RELATED PROBLEMS:
    - LeetCode 122: Multiple transactions allowed
    - LeetCode 123: At most 2 transactions
    - LeetCode 188: At most k transactions
    - LeetCode 309: With cooldown
    - LeetCode 714: With transaction fee
    """
