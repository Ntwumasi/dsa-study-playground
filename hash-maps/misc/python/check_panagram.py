"""
Check If the Sentence Is Pangram (LeetCode 1832)

PATTERN: Hash Set - Character Presence Tracking
- Use a set to track unique characters
- A pangram contains all 26 letters of the alphabet

TIME COMPLEXITY: O(n) - single pass through the string
SPACE COMPLEXITY: O(1) - set contains at most 26 characters

WHY THIS WORKS:
- Sets automatically handle duplicates
- We only need to check if we've seen all 26 letters
- No need to count frequencies, just presence
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        Check if sentence contains every letter of the alphabet at least once.

        Args:
            sentence: String containing only lowercase English letters

        Returns:
            True if sentence is a pangram, False otherwise

        Visual:
            sentence = "thequickbrownfoxjumpsoverthelazydog"

            Build set of unique characters:
            seen = {'t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', ...}

            After processing: len(seen) = 26 ✓

            Answer: True (it's a pangram!)

        Example 2:
            sentence = "leetcode"
            seen = {'l', 'e', 't', 'c', 'o', 'd'}
            len(seen) = 6 (missing 20 letters)
            Answer: False
        """
        # Convert sentence to set of unique characters
        seen = set(sentence)

        # Check if we have all 26 letters
        # (sentence only contains lowercase letters per problem constraints)
        return len(seen) == 26


def check_if_pangram_alphabet(sentence: str) -> bool:
    """
    Alternative: Check against alphabet set.

    More explicit about what we're checking.
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(sentence))


def check_if_pangram_bitmask(sentence: str) -> bool:
    """
    Alternative: Bitmask approach using bit manipulation.

    Use 26 bits to track which letters we've seen.
    TIME: O(n), SPACE: O(1) - just one integer
    """
    seen = 0  # 26-bit mask

    for char in sentence:
        # Map 'a'-'z' to bits 0-25
        bit_position = ord(char) - ord('a')
        # Set the corresponding bit
        seen |= (1 << bit_position)

    # Check if all 26 bits are set
    # (2^26 - 1) = 0b11111111111111111111111111 (26 ones)
    return seen == (1 << 26) - 1


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Example 1: Classic pangram
    sentence1 = "thequickbrownfoxjumpsoverthelazydog"
    print(f"'{sentence1[:20]}...': {sol.checkIfPangram(sentence1)}")  # True

    # Example 2: Not a pangram
    sentence2 = "leetcode"
    print(f"'{sentence2}': {sol.checkIfPangram(sentence2)}")  # False

    # Alternative approaches
    print(f"Alphabet check: {check_if_pangram_alphabet(sentence1)}")  # True
    print(f"Bitmask check: {check_if_pangram_bitmask(sentence1)}")  # True

    """
    HASH SET PATTERN FOR CHARACTER PROBLEMS:

    Common use cases:
    1. Check presence of all characters (pangram)
    2. Find unique characters
    3. Check for duplicates
    4. Find first non-repeating character

    Key insight:
    - Sets give O(1) lookup for character presence
    - For alphabet problems, max set size is 26 (constant space)
    - Bitmask is even more space-efficient for fixed character sets
    """
