class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}

        # add each occ to hmap as key
        for i in nums:
            if i in hmap.keys():
                hmap[i] += 1
            else:
                hmap[i] = 1
        # no element
        if len(nums) == 0:
            return 0
        
        res = 1
        # loop through each key
        for k in hmap.keys():
            curru = currd = k
            count = 1 # base case
            # search both upward and downward
            while curru + 1 in hmap.keys():
                count += 1
                curru += 1
            while currd - 1 in hmap.keys():
                count += 1
                currd -= 1
            if count > res:
                res = count
        
        return res




        