# Given two strings text1 and text2,
# return the length of their longest common subsequence.

# For example, 
# given text1 = "abcde" and text2 = "ace",
# return 3. Both strings share "ace" as a subsequence

def longestSubsequence(text1,text2):
    m = len(text1)
    n = len(text2)
    # initialize the 2d grid
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # the above initializes the 2d array, we add the +1 to take care of 
    # the base case
    # next lets start to populate the grid
    for i in range(1, m + 1):
        for j in range(1,n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    return dp[m][n]

print(longestSubsequence("abcde","ace"))
print(longestSubsequence("abc","def"))
print(longestSubsequence("AGGTAB","GXTXAYB"))