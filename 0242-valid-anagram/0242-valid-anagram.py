class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Use fixed-size array for lowercase English letters (more efficient than dict)
        count = [0] * 26
        
        # Count frequency of characters in s
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Decrement frequency based on characters in t
        for char in t:
            idx = ord(char) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        
        return True