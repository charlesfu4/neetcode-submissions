class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}

        for c in magazine:
            if c not in store:
                store[c] = 1
            else:
                store[c] += 1
        

        for c in ransomNote:
            if c in store.keys() and store[c] >=1:
                store[c] -= 1
            else:
                return False
        return True
            
        