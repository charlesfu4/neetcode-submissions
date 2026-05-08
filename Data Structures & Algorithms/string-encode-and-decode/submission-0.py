class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            # collect number before #
            while s[j] != '#':
                j += 1
            # integerize
            l = int(s[i:j])
            # shift the needles to the str
            i = j + 1
            j = i + l
            res.append(s[i:j])
            # shift i to j so it can repeat 
            i = j
        return res

            

