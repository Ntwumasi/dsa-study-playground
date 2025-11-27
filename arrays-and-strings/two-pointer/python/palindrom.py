"""
Valid Palindrome (LeetCode 125)

PATTERN: Two Pointer - Opposite Direction
- Use two pointers starting at opposite ends of string
- Compare characters moving inward toward the center

TIME COMPLEXITY: O(n) - traverse at most n/2 characters
SPACE COMPLEXITY: O(1) - only using two pointers

WHY THIS WORKS:
- A palindrome reads the same forwards and backwards
- By comparing characters from outside-in, we can detect mismatches early
- If all pairs match until pointers meet, it's a palindrome
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        s: Input string to check

    Returns:
        True if palindrome, False otherwise

    Visual:
        s = "racecar"

        Step 1: left=0, right=6 -> 'r' == 'r' ✓
        Step 2: left=1, right=5 -> 'a' == 'a' ✓
        Step 3: left=2, right=4 -> 'c' == 'c' ✓
        Step 4: left=3, right=3 -> pointers meet, done!
    """
    # Initialize pointers at opposite ends
    left = 0
    right = len(s) - 1

    # Loop until pointers meet in the middle
    while left < right:
        # If characters don't match, it's not a palindrome
        if s[left] != s[right]:
            return False

        # Move pointers toward the center
        left += 1
        right -= 1

    # All pairs matched - it's a palindrome!
    return True


def is_palindrome_alphanumeric(s: str) -> bool:
    """
    Check if a string is a palindrome, considering only alphanumeric characters
    and ignoring case (LeetCode's actual problem).

    Args:
        s: Input string with possible spaces and punctuation

    Returns:
        True if palindrome, False otherwise
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


# Test cases
if __name__ == "__main__":
    # Basic palindrome check
    print(is_palindrome("racecar"))    # True
    print(is_palindrome("racecars"))   # False
    print(is_palindrome("a"))          # True (single char)
    print(is_palindrome(""))           # True (empty string)

    # Alphanumeric version
    print(is_palindrome_alphanumeric("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome_alphanumeric("race a car"))                       # False
