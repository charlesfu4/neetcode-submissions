class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nzmul = 1
        zero_count = 0

        for i in nums:
            if i != 0:
                nzmul *= i
            else:
                zero_count += 1
        
        res = []
        for i in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                res.append(nzmul if i == 0 else 0)
            else:
                res.append(nzmul // i)
        return res

        
