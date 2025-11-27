"""
Longest Valid Parentheses (LeetCode 32)

PATTERN: Dynamic Programming - Linear 1D DP
- dp[i] = length of longest valid substring ENDING at index i
- Handle two cases: "()" and "))"

TIME COMPLEXITY: O(n) - single pass
SPACE COMPLEXITY: O(n) for DP array

WHY THIS WORKS:
- A valid substring at position i depends on previous valid substrings
- "()" is trivially valid and extends previous valid block
- "))" needs to find a matching "(" before the previous valid block
"""


class Solution:
    def longest_valid_parentheses(self, s: str) -> int:
        """
        Find length of longest valid parentheses substring.

        Args:
            s: String containing only '(' and ')'

        Returns:
            Length of longest valid (well-formed) parentheses substring

        Visual:
            s = "(()()"

            i=0: '(' -> can't end valid substring -> dp[0] = 0
            i=1: '(' -> can't end valid substring -> dp[1] = 0
            i=2: ')' -> s[1]='(' matches! -> dp[2] = dp[0] + 2 = 2
            i=3: '(' -> can't end valid substring -> dp[3] = 0
            i=4: ')' -> s[3]='(' matches! -> dp[4] = dp[2] + 2 = 4

            Answer: 4 -> "()()"

        Another example: s = "((()))"
            dp = [0, 0, 2, 0, 4, 6]
            Answer: 6
        """
        n = len(s)
        if n == 0:
            return 0

        # dp[i] = length of longest valid substring ending at index i
        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                # Case 1: "()" - previous char is '('
                if s[i - 1] == '(':
                    # Length = 2 + whatever valid block came before
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2

                # Case 2: "))" - need to find matching '(' before valid block
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # Position of potential matching '(' is: i - dp[i-1] - 1
                    # Length = previous valid block + 2 + any valid block before that
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] >= 2:
                        dp[i] += dp[i - dp[i - 1] - 2]

                max_len = max(max_len, dp[i])

        return max_len


def longest_valid_parentheses_stack(s: str) -> int:
    """
    Alternative: Stack-based approach.

    Stack stores indices, with -1 as initial base.
    TIME: O(n), SPACE: O(n)
    """
    stack = [-1]  # Base index for calculating lengths
    max_len = 0

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                # No matching '(', push current as new base
                stack.append(i)
            else:
                # Valid substring: current index - new top of stack
                max_len = max(max_len, i - stack[-1])

    return max_len


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longest_valid_parentheses("(()"))    # 2 -> "()"

    # Example 2
    print(sol.longest_valid_parentheses(")()())")) # 4 -> "()()"

    # Example 3
    print(sol.longest_valid_parentheses(""))       # 0

    # Example 4
    print(sol.longest_valid_parentheses("()(()"))  # 2

    # Stack approach
    print(longest_valid_parentheses_stack("(()"))  # 2

    """
    DP STATE TRANSITION EXPLAINED:

    Case 1: s[i] = ')' and s[i-1] = '('
    Pattern: ...()
    We found a "()" pair. Length = 2 + dp[i-2]
    Example: "xx()" at i=3 -> dp[3] = dp[1] + 2

    Case 2: s[i] = ')' and s[i-1] = ')'
    Pattern: ...))
    Need to check if there's a matching '(' BEFORE the previous valid block.

    Example: "((()))" at i=5
    - dp[4] = 4 (for "(())")
    - Position to check: i - dp[i-1] - 1 = 5 - 4 - 1 = 0
    - s[0] = '(' ✓
    - dp[5] = dp[4] + 2 = 6

    Visual:
    s =  ( ( ( ) ) )
    idx= 0 1 2 3 4 5
    dp = 0 0 0 2 4 6

    At i=5: dp[i-1]=4, check s[5-4-1]=s[0]='('
    """
