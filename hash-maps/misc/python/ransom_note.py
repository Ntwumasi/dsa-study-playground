"""
Ransom Note (LeetCode 383)

PATTERN: Hash Map - Character Frequency Matching
- Count character frequencies in magazine
- Check if magazine has enough of each character for ransom note

TIME COMPLEXITY: O(m + n) - count magazine + check ransom note
SPACE COMPLEXITY: O(1) - at most 26 lowercase letters

WHY THIS WORKS:
- Build frequency map from magazine (available characters)
- For each character in ransom note, decrement count
- If count goes negative, magazine doesn't have enough
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Check if ransom note can be constructed from magazine letters.

        Each letter in magazine can only be used once.

        Args:
            ransomNote: String to construct
            magazine: String providing available letters

        Returns:
            True if ransom note can be constructed

        Visual:
            ransomNote = "aa", magazine = "aab"

            Magazine frequency: {'a': 2, 'b': 1}

            Check ransom note:
            - 'a': need 1, have 2 -> use 1, now {'a': 1, 'b': 1}
            - 'a': need 1, have 1 -> use 1, now {'a': 0, 'b': 1}

            All characters satisfied!
            Answer: True

        Example 2:
            ransomNote = "aa", magazine = "ab"
            Magazine: {'a': 1, 'b': 1}
            - 'a': need 1, have 1 -> OK
            - 'a': need 1, have 0 -> FAIL!
            Answer: False
        """
        # Count available characters in magazine
        available = Counter(magazine)

        # Check each character in ransom note
        for char in ransomNote:
            if available[char] <= 0:
                return False
            available[char] -= 1

        return True


def can_construct_counter_subtraction(ransomNote: str, magazine: str) -> bool:
    """
    Alternative: Use Counter subtraction.

    Counter subtraction keeps only positive counts.
    If ransom - magazine is empty, we can construct it.
    """
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    # Subtract magazine from ransom note requirements
    # If anything remains, we're missing characters
    remaining = ransom_count - magazine_count
    return len(remaining) == 0


def can_construct_all_check(ransomNote: str, magazine: str) -> bool:
    """
    Alternative: Check all characters at once.

    More Pythonic but creates Counter for both strings.
    """
    ransom_count = Counter(ransomNote)
    magazine_count = Counter(magazine)

    # Check if magazine has enough of each character
    return all(
        magazine_count[char] >= count
        for char, count in ransom_count.items()
    )


def can_construct_string_replace(ransomNote: str, magazine: str) -> bool:
    """
    Original approach: String manipulation.

    TIME: O(m * n) - index() is O(m) for each of n characters
    SPACE: O(m) - creates new strings

    Less efficient but demonstrates the logic.
    """
    for char in ransomNote:
        if char not in magazine:
            return False
        # Find and remove the character from magazine
        location = magazine.index(char)
        magazine = magazine[:location] + magazine[location + 1:]
    return True


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Not enough 'a's
    print(sol.canConstruct("a", "b"))  # False

    # Example 2: Not enough 'a's
    print(sol.canConstruct("aa", "ab"))  # False

    # Example 3: Enough letters
    print(sol.canConstruct("aa", "aab"))  # True

    # Longer example
    note = "hello"
    mag = "ahelolbclo"
    print(f"'{note}' from '{mag}': {sol.canConstruct(note, mag)}")  # True

    # Alternative approaches
    print(f"Counter subtraction: {can_construct_counter_subtraction('aa', 'aab')}")
    print(f"All check: {can_construct_all_check('aa', 'aab')}")

    """
    FREQUENCY MATCHING PATTERN:

    Use cases:
    1. Ransom note / can construct string
    2. Anagram check (frequencies must be equal)
    3. Permutation in string (sliding window + frequency)

    Counter tips:
    - Counter(s)[char] returns 0 for missing chars (not KeyError)
    - Counter subtraction: only keeps positive counts
    - Counter intersection (&): min of counts
    - Counter union (|): max of counts

    Complexity comparison:
    | Approach           | Time    | Space |
    |--------------------|---------|-------|
    | Hash map           | O(m+n)  | O(1)  |
    | Counter subtract   | O(m+n)  | O(1)  |
    | String replace     | O(m*n)  | O(m)  |
    """
