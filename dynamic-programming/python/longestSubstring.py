"""
Longest Common Subsequence (LeetCode 1143)

PATTERN: Dynamic Programming - 2D Grid DP
- Compare two strings character by character
- Build solution using subproblem results

TIME COMPLEXITY: O(m * n) where m, n are string lengths
SPACE COMPLEXITY: O(m * n) for the DP table

WHY THIS WORKS:
- If characters match: LCS extends by 1 from diagonal
- If they don't match: LCS is max of excluding either character
- Building bottom-up ensures all subproblems are solved
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find length of longest common subsequence of two strings.

    A subsequence maintains relative order but doesn't need to be contiguous.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of longest common subsequence

    Visual:
        text1 = "abcde", text2 = "ace"

        DP table (dp[i][j] = LCS of text1[0:i] and text2[0:j]):

              ""  a  c  e
          ""   0  0  0  0
          a    0  1  1  1
          b    0  1  1  1
          c    0  1  2  2
          d    0  1  2  2
          e    0  1  2  3

        Answer: 3 (subsequence "ace")

    Recurrence:
        If text1[i-1] == text2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1  (extend the match)
        Else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])  (skip one char)
    """
    m, n = len(text1), len(text2)

    # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
    # Extra row/column for empty string base case
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                # Characters match: extend LCS from diagonal
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # No match: take best of excluding either character
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def longest_common_subsequence_string(text1: str, text2: str) -> str:
    """
    Variant: Return the actual LCS string, not just its length.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))


# Test cases
if __name__ == "__main__":
    # Example 1
    print(longest_common_subsequence("abcde", "ace"))  # 3 -> "ace"

    # Example 2
    print(longest_common_subsequence("abc", "def"))   # 0 -> no common chars

    # Example 3
    print(longest_common_subsequence("AGGTAB", "GXTXAYB"))  # 4 -> "GTAB"

    # Get actual subsequence
    print(longest_common_subsequence_string("abcde", "ace"))  # "ace"
    print(longest_common_subsequence_string("AGGTAB", "GXTXAYB"))  # "GTAB"

    """
    UNDERSTANDING THE DP TABLE:

    dp[i][j] represents the LCS of:
    - First i characters of text1: text1[0:i]
    - First j characters of text2: text2[0:j]

    Base case:
    - dp[0][j] = 0 (empty text1 has no common subsequence)
    - dp[i][0] = 0 (empty text2 has no common subsequence)

    Transition:
    - Characters match: dp[i][j] = dp[i-1][j-1] + 1
      We extend the LCS from the state before both chars were considered

    - Characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      We take the best LCS from either:
      * Excluding current char of text1
      * Excluding current char of text2
    """
