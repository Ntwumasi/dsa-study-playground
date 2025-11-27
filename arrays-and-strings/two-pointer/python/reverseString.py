"""
Reverse String (LeetCode 344)

PATTERN: Two Pointer - Opposite Direction with Swap
- Use two pointers at opposite ends
- Swap characters and move pointers inward

TIME COMPLEXITY: O(n) - traverse n/2 pairs
SPACE COMPLEXITY: O(1) - in-place swap, no extra space

WHY THIS WORKS:
- By swapping opposite elements and moving inward,
  each element ends up at its reversed position
- We only need n/2 swaps to reverse the entire array
"""


def reverse_string_inplace(s: list[str]) -> None:
    """
    Reverse a string IN-PLACE using two pointers.
    Modifies the input list directly (required by LeetCode).

    Args:
        s: List of characters to reverse

    Visual:
        ['h', 'e', 'l', 'l', 'o']
         L                   R     -> swap 'h' and 'o'
        ['o', 'e', 'l', 'l', 'h']
              L         R          -> swap 'e' and 'l'
        ['o', 'l', 'l', 'e', 'h']
                  L R              -> pointers meet, done!
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]

        # Move pointers toward center
        left += 1
        right -= 1


def reverse_string_return(s: str) -> str:
    """
    Reverse a string and return the result.
    (Alternative version that returns a new string)

    Args:
        s: String to reverse

    Returns:
        Reversed string
    """
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)


# Test cases
if __name__ == "__main__":
    # In-place version
    test1 = list("hello")
    reverse_string_inplace(test1)
    print(test1)  # ['o', 'l', 'l', 'e', 'h']

    test2 = list("Hannah")
    reverse_string_inplace(test2)
    print(test2)  # ['h', 'a', 'n', 'n', 'a', 'H']

    # Return version
    print(reverse_string_return("hello"))   # "olleh"
    print(reverse_string_return("world"))   # "dlrow"
