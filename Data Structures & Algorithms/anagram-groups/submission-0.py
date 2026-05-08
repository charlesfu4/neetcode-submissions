class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ohmap = {}
        for i in range(len(strs)):
            arr = [0] * 26
            for c in strs[i]:
                num = ord(c) - ord('a')
                arr[num] += 1
            key = tuple(arr)  # ✅ tuples are hashable, lists are not
            if key not in ohmap:
                ohmap[key] = [strs[i]]
            else:
                ohmap[key].append(strs[i])  # ✅ don't reassign — append returns None
        res = []
        for i in ohmap.values():
            res.append(i)
        return res