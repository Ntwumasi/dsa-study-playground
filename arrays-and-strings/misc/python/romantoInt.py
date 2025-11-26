def romanToInt(s: str) -> int:
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

    for char in reversed(s):
        curr = roman_map[char]
        if curr < prev:
            total -= curr  # subtract if a smaller numeral comes before a larger one
        else:
            total += curr
        prev = curr

    return total