def isPalindrome(s):
    # Initialize two pointers at the beginning and end of the string
    left = 0
    right = len(s) - 1

    # Loop until the pointers meet in the middle
    while left < right:
        # If characters at the two pointers don't match, it's not a palindrome
        if s[left] != s[right]:
            return False
        
        # Move the pointers toward the center
        left += 1
        right -= 1

    # If the loop completes without returning False, it is a palindrome
    return True

# Test cases
print(isPalindrome("racecar"))   # True ✅
print(isPalindrome("racecars"))  # False ❌