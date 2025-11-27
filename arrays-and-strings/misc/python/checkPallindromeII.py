"""
Valid Palindrome (LeetCode 125)

PATTERN: Two Pointers - Skip Non-Alphanumeric
- Use two pointers from both ends
- Skip non-alphanumeric characters
- Compare remaining characters (case-insensitive)

TIME COMPLEXITY: O(n) - single pass through string
SPACE COMPLEXITY: O(1) - only two pointers

WHY THIS WORKS:
- Non-alphanumeric characters don't affect palindrome status
- Case shouldn't matter for this definition
- Two pointers meet in middle if all characters match
"""


def checkIfPalindrome(s: str) -> bool:
    """
    Check if string is a palindrome (alphanumeric only, case-insensitive).

    Args:
        s: Input string

    Returns:
        True if palindrome considering only alphanumeric characters

    Visual:
        s = "A man, a plan, a canal: Panama"

        After filtering: "amanaplanacanalpanama"

        Two pointers:
        left=0 ('a'), right=20 ('a') -> match, move inward
        left=1 ('m'), right=19 ('m') -> match, move inward
        ...
        left=10 ('c'), right=10 ('c') -> meet in middle

        Answer: True

    Example 2:
        s = "race a car"
        After filtering: "raceacar"
        left=0 ('r'), right=7 ('r') -> match
        left=1 ('a'), right=6 ('a') -> match
        left=2 ('c'), right=5 ('c') -> match
        left=3 ('e'), right=4 ('a') -> NO MATCH!

        Answer: False
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


def valid_palindrome_clean(s: str) -> bool:
    """
    Alternative: Pre-process string first.

    TIME: O(n), SPACE: O(n) - creates new string

    Cleaner code but uses extra space.
    """
    # Filter to alphanumeric only, lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())

    # Check if equal to reverse
    return filtered == filtered[::-1]


def valid_palindrome_ii(s: str) -> bool:
    """
    LeetCode 680: Valid Palindrome II

    Can delete at most one character to make it a palindrome.

    Visual:
        s = "abca"
        - 'a' == 'a' (ends match)
        - 'b' != 'c' (mismatch!)
        - Try removing 'b': "aca" -> palindrome!
        - Or try removing 'c': "aba" -> palindrome!
        Answer: True
    """
    def is_palindrome_range(s: str, left: int, right: int) -> bool:
        """Check if s[left:right+1] is palindrome."""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try removing left character or right character
            return (is_palindrome_range(s, left + 1, right) or
                    is_palindrome_range(s, left, right - 1))
        left += 1
        right -= 1

    return True


# Test cases
if __name__ == "__main__":
    # Example 1: Valid palindrome with spaces and punctuation
    s1 = "A man, a plan, a canal: Panama"
    print(f"'{s1}': {checkIfPalindrome(s1)}")  # True

    # Example 2: Not a palindrome
    s2 = "race a car"
    print(f"'{s2}': {checkIfPalindrome(s2)}")  # False

    # Example 3: Empty or single character
    print(f"' ': {checkIfPalindrome(' ')}")  # True

    # Example 4: Only non-alphanumeric
    print(f"'.,': {checkIfPalindrome('.,')}")  # True

    # Clean approach
    print(f"\nClean approach: {valid_palindrome_clean(s1)}")  # True

    # Valid Palindrome II
    print(f"\nPalindrome II 'abca': {valid_palindrome_ii('abca')}")  # True
    print(f"Palindrome II 'abc': {valid_palindrome_ii('abc')}")  # False

    """
    PALINDROME PROBLEM VARIATIONS:

    1. Basic Palindrome (simple):
       - Just compare string with its reverse
       - O(n) time, O(n) space

    2. Valid Palindrome (this problem):
       - Consider only alphanumeric, ignore case
       - Two pointers with skip logic

    3. Valid Palindrome II (one deletion):
       - Can remove at most one character
       - When mismatch found, try both removals

    4. Longest Palindromic Substring:
       - Expand around center approach
       - O(n²) time, O(1) space

    5. Palindrome Partitioning:
       - Split string into palindrome substrings
       - DP or backtracking

    TWO-POINTER SKIP PATTERN:

    while left < right:
        # Skip invalid characters
        while left < right and not is_valid(s[left]):
            left += 1
        while left < right and not is_valid(s[right]):
            right -= 1

        # Process valid characters
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    """
