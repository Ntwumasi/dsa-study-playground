"""
Longest Substring Without Repeating Characters (LeetCode 3)

PATTERN: Sliding Window - Variable Size with Set/HashMap
- Window represents current substring without duplicates
- Expand by adding characters to the right
- Shrink when we encounter a duplicate character

TIME COMPLEXITY: O(n) - each character visited at most twice
SPACE COMPLEXITY: O(min(m, n)) where m is charset size (26 for lowercase)

WHY THIS WORKS:
- We maintain a "valid" window with no duplicates using a set
- When we find a duplicate, we shrink from the left until valid again
- Track the maximum valid window size throughout
"""


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Find length of longest substring without repeating characters.

        Args:
            s: Input string

        Returns:
            Length of longest valid substring

        Visual:
            s = "abcabcbb"

            Step 1: window="a"      seen={a}     max=1
            Step 2: window="ab"     seen={a,b}   max=2
            Step 3: window="abc"    seen={a,b,c} max=3
            Step 4: 'a' duplicate!
                    - remove 'a' from left
                    - window="bca"  seen={b,c,a} max=3
            Step 5: 'b' duplicate!
                    - remove 'b' from left
                    - window="cab"  seen={c,a,b} max=3
            ... and so on

            Final answer: 3 ("abc")
        """
        left = 0
        seen = set()  # Characters currently in our window
        max_len = 0

        for right in range(len(s)):
            # Shrink window while current char creates a duplicate
            while s[right] in seen:
                # Remove leftmost character from window
                seen.remove(s[left])
                left += 1

            # Add current character to window
            seen.add(s[right])

            # Update maximum length
            # Window size = right - left + 1
            max_len = max(max_len, right - left + 1)

        return max_len


def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized version using dict to jump left pointer directly.

    Instead of shrinking one character at a time, we can jump
    left pointer directly to the position after the duplicate.

    TIME: Still O(n), but faster in practice
    """
    char_index = {}  # Maps character to its most recent index
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        # If char was seen AND is within current window
        if char in char_index and char_index[char] >= left:
            # Jump left to position after the duplicate
            left = char_index[char] + 1

        # Update character's most recent position
        char_index[char] = right

        # Update maximum
        max_len = max(max_len, right - left + 1)

    return max_len


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Basic cases
    print(sol.length_of_longest_substring("abcabcbb"))  # 3 -> "abc"
    print(sol.length_of_longest_substring("bbbbb"))     # 1 -> "b"
    print(sol.length_of_longest_substring("pwwkew"))    # 3 -> "wke"

    # Edge cases
    print(sol.length_of_longest_substring(""))          # 0
    print(sol.length_of_longest_substring(" "))         # 1
    print(sol.length_of_longest_substring("abcdeab"))   # 5 -> "abcde" or "bcdea"

    # Optimized version
    print(length_of_longest_substring_optimized("abcabcbb"))  # 3

    """
    DETAILED WALKTHROUGH for "abcabcbb":

    right=0: char='a'
        seen={}, 'a' not in seen
        seen={'a'}, window="a", max=1

    right=1: char='b'
        seen={'a'}, 'b' not in seen
        seen={'a','b'}, window="ab", max=2

    right=2: char='c'
        seen={'a','b'}, 'c' not in seen
        seen={'a','b','c'}, window="abc", max=3

    right=3: char='a'
        seen={'a','b','c'}, 'a' IS in seen! -> SHRINK
        remove 'a', left=1, seen={'b','c'}
        now 'a' not in seen, add it
        seen={'b','c','a'}, window="bca", max=3

    right=4: char='b'
        seen={'b','c','a'}, 'b' IS in seen! -> SHRINK
        remove 'b', left=2, seen={'c','a'}
        add 'b'
        seen={'c','a','b'}, window="cab", max=3

    ... continues, max never exceeds 3

    ANSWER: 3
    """
