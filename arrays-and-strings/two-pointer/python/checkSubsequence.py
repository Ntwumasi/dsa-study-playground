def check_subsequence(s, t):
    # Initialize two pointers:
    # 'i' for string 's' (the smaller string we're trying to match)
    # 'j' for string 't' (the bigger string we're scanning through)
    i = j = 0

    # Loop while both pointers are within bounds
    while i < len(s) and j < len(t):
        # If characters at both pointers match, move pointer 'i' (we've found a match)
        if s[i] == t[j]:
            i += 1  # Move to next character in 's'
        
        # Always move pointer 'j' (we continue scanning 't' regardless of match)
        j += 1

    # After the loop, if we've matched all characters in 's',
    # then i should have moved to the end of 's'
    return i == len(s)

# Test cases
print(check_subsequence("abc", "ahbgdc"))  # True
print(check_subsequence("axc", "ahbgdc"))  # False
print(check_subsequence("ace", "abcde"))   # True

# s = "abc"
# t = "ahbgdc"

# Matched order:
#   s[0] = 'a' → found in t
#   s[1] = 'b' → found in t
#   s[2] = 'c' → found in t

# → i becomes 3  
# → len(s) = 3  
# → `i == len(s)` → ✅ return `True`

	# •	Time: O(n)
	# •	Space: O(1)