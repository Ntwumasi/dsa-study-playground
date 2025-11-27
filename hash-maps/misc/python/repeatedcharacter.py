"""
First Letter to Appear Twice (LeetCode 2351)

PATTERN: Hash Set - First Duplicate Detection
- Track seen characters in a set
- Return first character that's already in the set

TIME COMPLEXITY: O(n) - single pass, worst case scan entire string
SPACE COMPLEXITY: O(1) - at most 26 lowercase letters

WHY THIS WORKS:
- Set gives O(1) lookup for "have we seen this before?"
- First character found in set is our answer
- Guaranteed to find one (problem constraint)
"""


def repeatedChar(s: str) -> str:
    """
    Find the first letter that appears twice.

    Args:
        s: String of lowercase English letters (guaranteed duplicate exists)

    Returns:
        First character to appear twice

    Visual:
        s = "abccbaacz"

        Scan through:
        - 'a': not in seen -> add to seen = {'a'}
        - 'b': not in seen -> add to seen = {'a', 'b'}
        - 'c': not in seen -> add to seen = {'a', 'b', 'c'}
        - 'c': IN SEEN! -> return 'c'

        Answer: 'c' (first to repeat)

    Note: 'a' also repeats later, but 'c' repeats first.
    """
    seen = set()

    for char in s:
        if char in seen:
            return char
        seen.add(char)

    # Problem guarantees a duplicate exists
    return ""


def repeated_char_count(s: str) -> str:
    """
    Alternative: Using Counter (less efficient for this problem).

    This finds character that appears twice, but not necessarily
    the FIRST to appear twice. Included to show the difference.
    """
    from collections import Counter
    freq = Counter(s)

    # This returns ANY duplicate, not the first one!
    for char, count in freq.items():
        if count >= 2:
            return char
    return ""


def first_unique_char(s: str) -> int:
    """
    Related problem: First Unique Character (LeetCode 387)

    Find index of first character that appears exactly once.
    """
    from collections import Counter
    freq = Counter(s)

    for i, char in enumerate(s):
        if freq[char] == 1:
            return i

    return -1


# Test cases
if __name__ == "__main__":
    # Example 1
    s1 = "abccbaacz"
    print(f"s='{s1}': '{repeatedChar(s1)}'")  # 'c'

    # Example 2
    s2 = "abcdd"
    print(f"s='{s2}': '{repeatedChar(s2)}'")  # 'd'

    # Example 3: First letter repeats
    s3 = "aabb"
    print(f"s='{s3}': '{repeatedChar(s3)}'")  # 'a'

    # Related: First unique character
    s4 = "leetcode"
    print(f"First unique in '{s4}': index {first_unique_char(s4)}")  # 0 ('l')

    s5 = "loveleetcode"
    print(f"First unique in '{s5}': index {first_unique_char(s5)}")  # 2 ('v')

    """
    SET vs COUNTER FOR CHARACTER PROBLEMS:

    Use SET when:
    - Only need to track presence (seen/not seen)
    - Looking for first duplicate
    - Checking if character exists

    Use COUNTER when:
    - Need exact counts of each character
    - Finding most/least common
    - Comparing frequencies between strings

    Related problems:
    - First Letter to Appear Twice (this problem)
    - First Unique Character in String
    - Longest Substring Without Repeating Characters
    - Contains Duplicate

    SET MEMBERSHIP PATTERN:
        seen = set()
        for item in collection:
            if item in seen:
                # Found duplicate!
            seen.add(item)
    """
