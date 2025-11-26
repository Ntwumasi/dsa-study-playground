class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set(sentence)
        # note that set() will only contain unique characters

        return len(seen) == len(sentence)
        