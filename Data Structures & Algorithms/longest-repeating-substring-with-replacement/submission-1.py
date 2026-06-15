class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        L = 0
        max_freq = 0
        result = 0
        count = {}

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_freq = max(max_freq, count[s[R]])

            if R - L + 1 - max_freq > k: # if there is no enough k to use evict L and shrink L
                count[s[L]] -= 1
                L += 1
            
            result = max(result, R - L + 1)
            

        return result


        