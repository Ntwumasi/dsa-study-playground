"""
Best Time to Buy and Sell Stock with Transaction Fee (LeetCode 714)

PATTERN: Dynamic Programming - Two States
- Unlimited transactions allowed
- Each transaction has a fee
- Track two states: holding vs not holding

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) with 2D array, O(1) optimized

WHY THIS WORKS:
- At any point, we're either holding stock or not
- State transition: buy (pay price), sell (get price - fee)
- DP tracks max profit in each state
"""


def max_profit(prices: list[int], fee: int) -> int:
    """
    Find max profit with unlimited transactions and transaction fee.

    The fee is paid once per transaction (buy + sell = 1 transaction).
    We deduct fee when selling (could also deduct when buying).

    Args:
        prices: Stock prices on each day
        fee: Fee per complete transaction

    Returns:
        Maximum profit after fees

    Visual:
        prices = [1, 3, 2, 8, 4, 9], fee = 2

        Optimal strategy:
        - Buy at 1, sell at 8, profit = 8-1-2 = 5
        - Buy at 4, sell at 9, profit = 9-4-2 = 3
        - Total: 5 + 3 = 8

        State tracking:
        dp[i][0] = max profit on day i when NOT holding stock
        dp[i][1] = max profit on day i when HOLDING stock
    """
    n = len(prices)
    if n == 0:
        return 0

    # dp[i][0] = max profit at day i, NOT holding stock
    # dp[i][1] = max profit at day i, HOLDING stock
    dp = [[0] * 2 for _ in range(n)]

    # Base case (day 0)
    dp[0][0] = 0              # Not holding: no profit yet
    dp[0][1] = -prices[0]     # Holding: bought today, profit is negative

    for i in range(1, n):
        # Not holding: either stay not holding OR sell today
        dp[i][0] = max(
            dp[i - 1][0],                    # Stay not holding
            dp[i - 1][1] + prices[i] - fee   # Sell today (pay fee)
        )

        # Holding: either stay holding OR buy today
        dp[i][1] = max(
            dp[i - 1][1],                    # Stay holding
            dp[i - 1][0] - prices[i]         # Buy today
        )

    # Final answer: not holding (can't end with unsold stock)
    return dp[n - 1][0]


def max_profit_optimized(prices: list[int], fee: int) -> int:
    """
    Space-optimized version using O(1) space.

    Only need previous day's values.
    """
    if not prices:
        return 0

    not_holding = 0           # dp[i][0]
    holding = -prices[0]      # dp[i][1]

    for i in range(1, len(prices)):
        # Calculate new states
        new_not_holding = max(not_holding, holding + prices[i] - fee)
        new_holding = max(holding, not_holding - prices[i])

        # Update states
        not_holding = new_not_holding
        holding = new_holding

    return not_holding


# Test cases
if __name__ == "__main__":
    # Example 1
    prices1 = [1, 3, 2, 8, 4, 9]
    fee1 = 2
    print(f"Prices {prices1}, fee={fee1}: {max_profit(prices1, fee1)}")  # 8

    # Example 2
    prices2 = [1, 3, 7, 5, 10, 3]
    fee2 = 3
    print(f"Prices {prices2}, fee={fee2}: {max_profit(prices2, fee2)}")  # 6

    # Optimized version
    print(f"Optimized: {max_profit_optimized(prices1, fee1)}")  # 8

    """
    STATE TRANSITION DIAGRAM:

    NOT_HOLDING ──────buy────────► HOLDING
         ▲                            │
         │                            │
         │                            │
         └───────sell (pay fee)───────┘

    Transitions:
    - not_holding[i] = max(not_holding[i-1], holding[i-1] + price - fee)
    - holding[i] = max(holding[i-1], not_holding[i-1] - price)

    KEY INSIGHT:
    The fee discourages frequent trading. Without fees, we'd trade
    every time there's a price increase. With fees, we only trade
    when profit > fee.
    """
