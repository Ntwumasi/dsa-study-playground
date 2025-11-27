"""
Longest Palindromic Substring (LeetCode 5)

PATTERN: Expand Around Center
- Every palindrome has a center (single char or two chars)
- Expand outward from each possible center
- Track the longest palindrome found

TIME COMPLEXITY: O(n²) - O(n) centers, each expansion is O(n)
SPACE COMPLEXITY: O(1) - only storing the result

WHY THIS WORKS:
- A palindrome mirrors around its center
- We can find all palindromes by checking every possible center
- Odd-length palindromes: single character center
- Even-length palindromes: two character center
"""


class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring.

        Args:
            s: Input string

        Returns:
            Longest palindromic substring

        Visual:
            s = "babad"

            Center at index 0 ('b'):
                Odd: "b" (length 1)
                Even: "ba" -> not palindrome

            Center at index 1 ('a'):
                Odd: "bab" (length 3) ← found palindrome!
                Even: "ab" -> not palindrome

            Center at index 2 ('b'):
                Odd: "aba" (length 3)
                Even: "ba" -> not palindrome

            ... and so on

            Answer: "bab" or "aba" (both length 3)
        """
        def expand_around_center(left: int, right: int) -> str:
            """
            Expand outward while characters match.

            Args:
                left: Left pointer (starting position)
                right: Right pointer (starting position)
                       For odd palindrome: left == right
                       For even palindrome: right == left + 1

            Returns:
                Longest palindrome found from this center
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # After loop, left and right are one past the palindrome
            # Valid palindrome is s[left+1 : right]
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            # Check odd-length palindrome (single character center)
            odd = expand_around_center(i, i)

            # Check even-length palindrome (two character center)
            even = expand_around_center(i, i + 1)

            # Update longest if we found a longer palindrome
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest


def longest_palindrome_dp(s: str) -> str:
    """
    Alternative: Dynamic Programming approach.

    dp[i][j] = True if s[i:j+1] is a palindrome

    TIME: O(n²)
    SPACE: O(n²) for the DP table
    """
    n = len(s)
    if n == 0:
        return ""

    # dp[i][j] = True if s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    start = 0
    max_len = 1

    # Check substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2

    # Check substrings of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # s[i:j+1] is palindrome if:
            # 1. s[i] == s[j], AND
            # 2. s[i+1:j] is palindrome (dp[i+1][j-1])
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length

    return s[start:start + max_len]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(sol.longest_palindrome("babad"))  # "bab" or "aba"

    # Example 2
    print(sol.longest_palindrome("cbbd"))   # "bb"

    # Single character
    print(sol.longest_palindrome("a"))      # "a"

    # All same characters
    print(sol.longest_palindrome("aaaa"))   # "aaaa"

    # DP approach
    print(longest_palindrome_dp("babad"))   # "bab" or "aba"

    """
    EXPAND AROUND CENTER EXPLAINED:

    For string "abcba":
    - Center at 'c' (index 2)
    - Expand: s[2] == s[2] ✓ -> "c"
    - Expand: s[1] == s[3] -> 'b' == 'b' ✓ -> "bcb"
    - Expand: s[0] == s[4] -> 'a' == 'a' ✓ -> "abcba"
    - Expand: left=-1 -> stop

    Total 2n-1 centers to check:
    - n single character centers (for odd-length)
    - n-1 two character centers (for even-length)
    """
