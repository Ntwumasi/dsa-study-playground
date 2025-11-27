"""
Min Cost Climbing Stairs (LeetCode 746)

PATTERN: Dynamic Programming - Linear 1D DP with Minimization
- Each step has a cost
- Can climb 1 or 2 steps
- Find minimum total cost to reach the top

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) with array, O(1) optimized

WHY THIS WORKS:
- To reach step i, we came from either (i-1) or (i-2)
- Choose the path with minimum cost
- dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
"""


def min_cost_climbing_stairs(cost: list[int]) -> int:
    """
    Find minimum cost to climb to the top of the stairs.

    You can start from index 0 or index 1.
    The "top" is beyond the last step (index n).

    Args:
        cost: Cost of each step

    Returns:
        Minimum total cost to reach the top

    Visual:
        cost = [10, 15, 20]
        indices: 0   1   2   TOP

        Options to reach TOP (index 3):
        - Start at 0, pay 10, jump 2 to index 2, pay 20 → total 30
        - Start at 1, pay 15, jump 2 to TOP → total 15 ✓

        dp[0] = 0  (cost to reach index 0, haven't paid yet)
        dp[1] = 0  (cost to reach index 1, haven't paid yet)
        dp[2] = min(dp[1]+cost[1], dp[0]+cost[0]) = min(15, 10) = 10
        dp[3] = min(dp[2]+cost[2], dp[1]+cost[1]) = min(10+20, 0+15) = 15

        Answer: 15
    """
    n = len(cost)

    # dp[i] = minimum cost to reach step i (before paying cost[i])
    dp = [0] * (n + 1)

    # We can start at index 0 or 1 for free
    # dp[0] = dp[1] = 0

    # Fill from step 2 to step n (top)
    for i in range(2, n + 1):
        # Option 1: Came from step (i-1), paid cost[i-1]
        # Option 2: Came from step (i-2), paid cost[i-2]
        from_one_step = dp[i - 1] + cost[i - 1]
        from_two_steps = dp[i - 2] + cost[i - 2]
        dp[i] = min(from_one_step, from_two_steps)

    return dp[n]


def min_cost_climbing_stairs_optimized(cost: list[int]) -> int:
    """
    Space-optimized version using O(1) space.
    """
    n = len(cost)

    prev2 = 0  # Cost to reach (i-2)
    prev1 = 0  # Cost to reach (i-1)

    for i in range(2, n + 1):
        curr = min(prev1 + cost[i - 1], prev2 + cost[i - 2])
        prev2 = prev1
        prev1 = curr

    return prev1


# Test cases
if __name__ == "__main__":
    # Example 1
    cost1 = [10, 15, 20]
    print(f"Cost {cost1}: {min_cost_climbing_stairs(cost1)}")  # 15
    # Start at index 1, pay 15, jump to top

    # Example 2
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f"Cost {cost2}: {min_cost_climbing_stairs(cost2)}")  # 6
    # Optimal path: pay at indices 0, 2, 3, 4, 6, 7, 9 = 1+1+1+1+1+1+0 = 6

    # Verify optimized version
    print(f"Optimized: {min_cost_climbing_stairs_optimized(cost2)}")  # 6

    """
    STATE TRANSITION:

    State: dp[i] = minimum cost to REACH step i

    Transition:
    dp[i] = min(
        dp[i-1] + cost[i-1],  # Came from one step back
        dp[i-2] + cost[i-2]   # Came from two steps back
    )

    Note: We pay the cost WHEN LEAVING a step, not when arriving.
    That's why reaching step i means we haven't paid cost[i] yet.

    Base cases:
    - dp[0] = 0 (can start here for free)
    - dp[1] = 0 (can start here for free)
    """
