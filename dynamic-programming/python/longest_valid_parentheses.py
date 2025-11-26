class Solution:  
    def longestValidParentheses(self,s: str) -> int:
        n = len(s)
        dp = [0] * n  # dp[i] stores the length of the longest valid substring ending at index i
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case: "()", just add 2 to what we had two positions back
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # Case: "))" pattern, try to match an opening before the previous valid block
                    dp[i] = dp[i - 1] + 2
                    if i - dp[i - 1] >= 2:
                        dp[i] += dp[i - dp[i - 1] - 2]
                max_len = max(max_len, dp[i])

        return max_len