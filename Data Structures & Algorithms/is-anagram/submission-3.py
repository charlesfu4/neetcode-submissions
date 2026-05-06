class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hmap = {}

        # fill up hashmap with one side of chars
        for c in s:
            if c not in hmap:
                hmap[c] = 1
            else:
                hmap[c] += 1
        
        # loop through keys and deduct counts
        for c in t:
            if c in hmap and hmap[c] > 0:
                hmap[c] -= 1
            else:
                return False
        
        for val in hmap.values():
            if val >= 1:
                return False
            
        return True
        

        