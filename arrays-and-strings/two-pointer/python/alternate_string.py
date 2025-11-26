class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # loop through the strings using two pointers
        m = len(word1)
        n = len(word2)
        i = j = 0
        merged = []
        # above i'm setting up my variables
        while i < m and j < n:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        while i < m:
            merged.append(word1[i])
            i += 1
        while j < n:
            merged.append(word2[j])
            j += 1
        
        return ''.join(merged)
        
