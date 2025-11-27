"""
Backspace String Compare (LeetCode 844)

PATTERN: Stack - Process with Undo Operations
- Use stack to process characters
- '#' means backspace (undo last character)
- Compare final results

TIME COMPLEXITY: O(n + m) - process both strings
SPACE COMPLEXITY: O(n + m) - stack storage for each string

WHY THIS WORKS:
- Stack perfectly models character insertion and deletion
- Push normal characters, pop on backspace
- Final stack content is the resulting string
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Compare two strings after processing backspaces.

        '#' represents a backspace (deletes previous character).

        Args:
            s: First string with possible backspaces
            t: Second string with possible backspaces

        Returns:
            True if strings are equal after processing backspaces

        Visual:
            s = "ab#c", t = "ad#c"

            Process s:
            - 'a': stack = ['a']
            - 'b': stack = ['a', 'b']
            - '#': stack = ['a']  (pop 'b')
            - 'c': stack = ['a', 'c']
            Result: "ac"

            Process t:
            - 'a': stack = ['a']
            - 'd': stack = ['a', 'd']
            - '#': stack = ['a']  (pop 'd')
            - 'c': stack = ['a', 'c']
            Result: "ac"

            Compare: "ac" == "ac" -> True
        """
        def build(string: str) -> str:
            """Process string and return result after backspaces."""
            stack = []

            for char in string:
                if char != "#":
                    # Normal character - add to stack
                    stack.append(char)
                elif stack:
                    # Backspace and stack not empty - remove last char
                    stack.pop()
                # If '#' and stack empty, do nothing (can't delete nothing)

            return "".join(stack)

        return build(s) == build(t)


def backspace_compare_two_pointer(s: str, t: str) -> bool:
    """
    Alternative: Two-pointer approach from the end.

    TIME: O(n + m), SPACE: O(1)

    Process both strings from right to left.
    Skip characters that will be deleted by backspaces.
    """
    def next_valid_index(string: str, index: int) -> int:
        """Find next valid character index (skipping backspaced chars)."""
        backspaces = 0

        while index >= 0:
            if string[index] == '#':
                backspaces += 1
                index -= 1
            elif backspaces > 0:
                # This character is deleted by a backspace
                backspaces -= 1
                index -= 1
            else:
                # Valid character
                break

        return index

    # Start from end of both strings
    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        # Find next valid character in each string
        i = next_valid_index(s, i)
        j = next_valid_index(t, j)

        # Compare characters (or check if both exhausted)
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            # One string has more characters than the other
            return False

        i -= 1
        j -= 1

    return True


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Equal after backspaces
    print(sol.backspaceCompare("ab#c", "ad#c"))  # True -> "ac" == "ac"

    # Example 2: Equal
    print(sol.backspaceCompare("ab##", "c#d#"))  # True -> "" == ""

    # Example 3: Not equal
    print(sol.backspaceCompare("a#c", "b"))  # False -> "c" != "b"

    # Example 4: Multiple backspaces
    print(sol.backspaceCompare("a##c", "#a#c"))  # True -> "c" == "c"

    # Two pointer approach
    print(f"\nTwo-pointer: {backspace_compare_two_pointer('ab#c', 'ad#c')}")  # True

    """
    STACK PATTERN FOR UNDO OPERATIONS:

    Perfect use cases:
    1. Backspace string compare (this problem)
    2. Text editor with undo
    3. Browser back button
    4. Expression evaluation with parentheses

    Pattern:
        stack = []
        for item in input:
            if is_normal(item):
                stack.append(item)
            elif is_undo(item) and stack:
                stack.pop()

    TWO-POINTER OPTIMIZATION:

    When we only need to compare (not build) the result:
    - Process from right to left
    - Skip characters that will be backspaced
    - Compare character by character
    - O(1) space instead of O(n)

    EDGE CASES:
    - Backspace at start (nothing to delete)
    - Multiple consecutive backspaces
    - Empty result after all backspaces
    - Strings of different original lengths but same result
    """
