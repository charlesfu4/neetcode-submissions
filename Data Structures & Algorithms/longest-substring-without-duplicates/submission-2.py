class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        window = set()
        L = 0
        window.add(s[L])
        max_len = 1

        for R in range(1, len(s)):
            while s[R] in window and L < R:
                window.remove(s[L])
                L += 1
                window.add(s[L])

            else:
                window.add(s[R])
            
            max_len = max(max_len, R - L + 1)
        
        return max_len

        