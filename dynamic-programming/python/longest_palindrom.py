class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # valid palindromic substring

        longest = ""
        for i in range(len(s)):
            # Odd length (single char center)
            odd = expandAroundCenter(i, i)
            # Even length (two char center)
            even = expandAroundCenter(i, i + 1)

            # Keep the longer one
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest