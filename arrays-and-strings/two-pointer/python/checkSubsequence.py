"""
Is Subsequence (LeetCode 392)

PATTERN: Two Pointer - Same Direction on Two Strings
- Use one pointer for the subsequence (s), one for the main string (t)
- Only advance the subsequence pointer when we find a match
- Always advance the main string pointer

TIME COMPLEXITY: O(n) where n = len(t) - single pass through t
SPACE COMPLEXITY: O(1) - only two pointers

WHY THIS WORKS:
- A subsequence must maintain relative order (but not be contiguous)
- By scanning t from left to right, we find characters in order
- If we can match all characters of s (in order), s is a subsequence
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    Check if s is a subsequence of t.

    A subsequence is formed by deleting some (or no) characters from t
    without changing the relative order of remaining characters.

    Args:
        s: Potential subsequence string
        t: Main string to search in

    Returns:
        True if s is a subsequence of t

    Visual:
        s = "abc"
        t = "ahbgdc"

        t: a h b g d c
           ^           s[0]='a' matches! i=1
             ^         s[1]='b'? no match
               ^       s[1]='b' matches! i=2
                 ^     s[2]='c'? no match
                   ^   s[2]='c'? no match
                     ^ s[2]='c' matches! i=3

        i == len(s) → True (found all characters in order)
    """
    # Edge case: empty string is always a subsequence
    if not s:
        return True

    i = 0  # Pointer for subsequence s
    j = 0  # Pointer for main string t

    # Scan through t looking for characters of s
    while i < len(s) and j < len(t):
        # If characters match, move s pointer (we found this character)
        if s[i] == t[j]:
            i += 1

        # Always move t pointer (continue scanning)
        j += 1

    # If we matched all characters in s, i will equal len(s)
    return i == len(s)


def is_subsequence_recursive(s: str, t: str) -> bool:
    """
    Recursive solution (less efficient but educational).

    TIME: O(n) - same as iterative
    SPACE: O(n) - recursion stack depth
    """
    # Base cases
    if not s:
        return True  # Empty string is always a subsequence
    if not t:
        return False  # Non-empty s can't be subsequence of empty t

    # If first characters match, check rest of both strings
    if s[0] == t[0]:
        return is_subsequence_recursive(s[1:], t[1:])

    # Otherwise, skip this character in t and continue
    return is_subsequence_recursive(s, t[1:])


# Test cases
if __name__ == "__main__":
    # Basic test cases
    print(is_subsequence("abc", "ahbgdc"))  # True - a,b,c appear in order
    print(is_subsequence("axc", "ahbgdc"))  # False - no 'x' in t
    print(is_subsequence("ace", "abcde"))   # True - a,c,e appear in order

    # Edge cases
    print(is_subsequence("", "ahbgdc"))     # True - empty is always subsequence
    print(is_subsequence("abc", ""))        # False - can't find in empty string
    print(is_subsequence("", ""))           # True - empty is subsequence of empty

    # Same strings
    print(is_subsequence("abc", "abc"))     # True - identical strings

    """
    COMPLEXITY ANALYSIS:

    Time: O(n) where n = len(t)
    - We iterate through t at most once
    - Each character comparison is O(1)

    Space: O(1)
    - Only using two integer pointers
    - No additional data structures

    FOLLOW-UP (LeetCode asks this):
    If there are many incoming s strings to check against the same t,
    preprocess t into a hashmap of {char: [indices]} for O(s) per query.
    """
