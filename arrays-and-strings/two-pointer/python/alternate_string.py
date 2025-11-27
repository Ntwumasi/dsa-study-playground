"""
Merge Strings Alternately (LeetCode 1768)

PATTERN: Two Pointer - Same Direction on Two Strings
- Use one pointer for each string
- Alternate taking characters from each string
- Handle remaining characters when lengths differ

TIME COMPLEXITY: O(n + m) where n, m are string lengths
SPACE COMPLEXITY: O(n + m) for the result

WHY THIS WORKS:
- We process both strings in parallel using two pointers
- By appending alternately, we achieve the interleaved pattern
- After one string is exhausted, we append the rest of the other
"""


class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings by alternating characters.

        Args:
            word1: First string
            word2: Second string

        Returns:
            Merged string with alternating characters

        Visual:
            word1 = "abc"
            word2 = "pqrs"

            Step 1: take 'a' from word1 → "a"
            Step 2: take 'p' from word2 → "ap"
            Step 3: take 'b' from word1 → "apb"
            Step 4: take 'q' from word2 → "apbq"
            Step 5: take 'c' from word1 → "apbqc"
            Step 6: take 'r' from word2 → "apbqcr"
            Step 7: word1 exhausted, append 's' → "apbqcrs"
        """
        m, n = len(word1), len(word2)
        i = j = 0
        merged = []

        # Alternate while both strings have characters
        while i < m and j < n:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from word1 (if any)
        while i < m:
            merged.append(word1[i])
            i += 1

        # Append remaining characters from word2 (if any)
        while j < n:
            merged.append(word2[j])
            j += 1

        return ''.join(merged)


def merge_alternately_pythonic(word1: str, word2: str) -> str:
    """
    Pythonic solution using itertools.

    Uses zip_longest to handle different lengths elegantly.
    """
    from itertools import zip_longest

    result = []
    for c1, c2 in zip_longest(word1, word2, fillvalue=''):
        result.append(c1 + c2)
    return ''.join(result)


def merge_alternately_one_liner(word1: str, word2: str) -> str:
    """
    One-liner using zip_longest (for fun, not recommended for readability).
    """
    from itertools import zip_longest
    return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Equal length strings
    print(sol.merge_alternately("abc", "xyz"))     # "axbycz"

    # word1 shorter
    print(sol.merge_alternately("ab", "pqrs"))     # "apbqrs"

    # word2 shorter
    print(sol.merge_alternately("abcd", "pq"))     # "apbqcd"

    # One empty string
    print(sol.merge_alternately("", "xyz"))        # "xyz"
    print(sol.merge_alternately("abc", ""))        # "abc"

    # Pythonic versions
    print(merge_alternately_pythonic("abc", "pqrs"))  # "apbqcrs"
    print(merge_alternately_one_liner("abc", "pqrs")) # "apbqcrs"
