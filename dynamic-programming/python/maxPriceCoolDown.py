"""
Best Time to Buy and Sell Stock with Cooldown (LeetCode 309)

PATTERN: Dynamic Programming - State Machine
- Multiple transactions allowed
- After selling, must wait 1 day before buying again (cooldown)
- Track three states: holding, just sold, resting

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) with arrays, O(1) optimized

STATE MACHINE:
- HOLD: Currently holding a stock
- SOLD: Just sold a stock today (must cooldown tomorrow)
- REST: Not holding, not in cooldown (can buy tomorrow)
"""

from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Find max profit with unlimited transactions but 1-day cooldown after selling.

        Args:
            prices: Stock prices on each day

        Returns:
            Maximum profit achievable

        Visual State Machine:
                    ┌──────────────────────┐
                    │         REST         │
                    │   (can buy or rest)  │
                    └──────────┬───────────┘
                               │ buy
                               ▼
                    ┌──────────────────────┐
                    │         HOLD         │◄────┐
                    │  (holding stock)     │     │ hold
                    └──────────┬───────────┘─────┘
                               │ sell
                               ▼
                    ┌──────────────────────┐
                    │         SOLD         │
                    │   (just sold, must   │
                    │    cooldown)         │
                    └──────────┬───────────┘
                               │ wait (cooldown)
                               ▼
                          back to REST
        """
        if not prices:
            return 0

        n = len(prices)

        # State arrays
        hold = [0] * n  # Max profit when holding stock at end of day i
        sold = [0] * n  # Max profit when just sold at end of day i
        rest = [0] * n  # Max profit when resting (no stock) at end of day i

        # Base cases (day 0)
        hold[0] = -prices[0]  # Bought on day 0
        sold[0] = 0           # Can't sell on day 0 (nothing to sell)
        rest[0] = 0           # Resting on day 0

        for i in range(1, n):
            # HOLD: either continue holding OR buy today (from rest state)
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])

            # SOLD: sell today (must have been holding yesterday)
            sold[i] = hold[i - 1] + prices[i]

            # REST: either continue resting OR finished cooldown from selling
            rest[i] = max(rest[i - 1], sold[i - 1])

        # Final answer: max of sold or rest (can't end while holding)
        return max(sold[-1], rest[-1])


def max_profit_optimized(prices: List[int]) -> int:
    """
    Space-optimized version using O(1) space.
    """
    if not prices:
        return 0

    hold = -prices[0]
    sold = 0
    rest = 0

    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest

        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)

    return max(sold, rest)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    prices1 = [1, 2, 3, 0, 2]
    print(f"Prices {prices1}: {sol.max_profit(prices1)}")  # 3
    # Buy at 1, sell at 3, cooldown, buy at 0, sell at 2
    # Profit: (3-1) + (2-0) = 2 + 2 = 4? Let's trace:
    # Actually: buy@1, sell@3 (+2), cool, buy@0, sell@2 (+2) = 4
    # Wait, the example says 3. Let me re-trace...
    # Buy@1, sell@2 (+1), cool, buy@0, sell@2 (+2) = 3

    # Example 2: No cooldown needed
    prices2 = [1, 2, 3, 4]
    print(f"Prices {prices2}: {sol.max_profit(prices2)}")  # 3

    # Optimized version
    print(f"Optimized: {max_profit_optimized(prices1)}")

    """
    STATE TRANSITIONS:

    From any state, what can happen tomorrow?

    HOLD[i] = max(
        HOLD[i-1],              # Continue holding
        REST[i-1] - prices[i]   # Buy today (must have been resting)
    )

    SOLD[i] = HOLD[i-1] + prices[i]  # Sell today (was holding)

    REST[i] = max(
        REST[i-1],              # Continue resting
        SOLD[i-1]               # Finished 1-day cooldown
    )

    Note: Can't go from SOLD directly to HOLD (cooldown required!)
    """
