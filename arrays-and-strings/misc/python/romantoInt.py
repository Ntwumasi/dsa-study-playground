"""
Roman to Integer (LeetCode 13)

PATTERN: Right-to-Left Iteration with Subtraction Rule
- Process from right to left
- If current value < previous value, subtract (subtraction rule)
- Otherwise, add to total

TIME COMPLEXITY: O(n) - single pass through string
SPACE COMPLEXITY: O(1) - fixed size hash map

WHY THIS WORKS:
- Roman numerals are additive (III = 1+1+1 = 3)
- Except when smaller precedes larger (IV = 5-1 = 4)
- Reading right-to-left makes subtraction rule easy to detect
"""


def romanToInt(s: str) -> int:
    """
    Convert Roman numeral to integer.

    Roman numeral rules:
    - I=1, V=5, X=10, L=50, C=100, D=500, M=1000
    - Normally additive (VI = 5+1 = 6)
    - Subtraction cases: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900

    Args:
        s: Roman numeral string (1 to 3999)

    Returns:
        Integer value

    Visual:
        s = "MCMXCIV" (1994)

        Process right to left:
        char: V  I  C  X  M  C  M
        val:  5  1  100 10 1000 100 1000

        V: prev=0, 5>=0 -> total=5, prev=5
        I: prev=5, 1<5 -> total=5-1=4, prev=1
        C: prev=1, 100>=1 -> total=4+100=104, prev=100
        X: prev=100, 10<100 -> total=104-10=94, prev=10
        M: prev=10, 1000>=10 -> total=94+1000=1094, prev=1000
        C: prev=1000, 100<1000 -> total=1094-100=994, prev=100
        M: prev=100, 1000>=100 -> total=994+1000=1994, prev=1000

        Answer: 1994
    """
    # Roman numeral value mapping
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev = 0

    # Process from right to left
    for char in reversed(s):
        curr = roman_map[char]

        if curr < prev:
            # Subtraction case (e.g., IV, IX, XL, XC, CD, CM)
            total -= curr
        else:
            # Normal addition
            total += curr

        prev = curr

    return total


def roman_to_int_left_to_right(s: str) -> int:
    """
    Alternative: Left-to-right with lookahead.

    Check if next character is larger (subtraction case).
    """
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0

    for i in range(len(s)):
        curr = roman_map[s[i]]

        # If next char exists and is larger, this is subtraction case
        if i + 1 < len(s) and curr < roman_map[s[i + 1]]:
            total -= curr
        else:
            total += curr

    return total


def int_to_roman(num: int) -> str:
    """
    LeetCode 12: Integer to Roman

    Convert integer to Roman numeral.
    """
    # Value-symbol pairs in descending order
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = []

    for value, symbol in values:
        # Add as many of this symbol as possible
        while num >= value:
            result.append(symbol)
            num -= value

    return ''.join(result)


# Test cases
if __name__ == "__main__":
    # Example 1
    print(f"III = {romanToInt('III')}")  # 3

    # Example 2
    print(f"LVIII = {romanToInt('LVIII')}")  # 58 (L=50, V=5, III=3)

    # Example 3
    print(f"MCMXCIV = {romanToInt('MCMXCIV')}")  # 1994

    # Subtraction cases
    print(f"\nSubtraction cases:")
    print(f"IV = {romanToInt('IV')}")   # 4
    print(f"IX = {romanToInt('IX')}")   # 9
    print(f"XL = {romanToInt('XL')}")   # 40
    print(f"XC = {romanToInt('XC')}")   # 90
    print(f"CD = {romanToInt('CD')}")   # 400
    print(f"CM = {romanToInt('CM')}")   # 900

    # Left-to-right approach
    print(f"\nLeft-to-right: {roman_to_int_left_to_right('MCMXCIV')}")  # 1994

    # Integer to Roman
    print(f"\n1994 -> {int_to_roman(1994)}")  # MCMXCIV
    print(f"58 -> {int_to_roman(58)}")  # LVIII

    """
    ROMAN NUMERAL RULES:

    Basic symbols:
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

    Subtraction combinations (6 cases):
    IV = 4   (5 - 1)
    IX = 9   (10 - 1)
    XL = 40  (50 - 10)
    XC = 90  (100 - 10)
    CD = 400 (500 - 100)
    CM = 900 (1000 - 100)

    WHY RIGHT-TO-LEFT IS ELEGANT:

    Left-to-right requires lookahead:
    - "Is next char larger? If so, subtract current"
    - Need bounds checking for i+1

    Right-to-left uses previous value:
    - "Is current smaller than what we just saw? If so, subtract"
    - No lookahead needed, cleaner code

    GENERAL PATTERN:
    When processing sequential data where current decision depends
    on neighbors, sometimes reverse iteration simplifies logic.

    INT TO ROMAN (GREEDY):
    Process from largest to smallest value.
    Use as many of each symbol as possible before moving to smaller.
    Include subtraction combinations (900, 400, 90, 40, 9, 4) in the list.
    """
