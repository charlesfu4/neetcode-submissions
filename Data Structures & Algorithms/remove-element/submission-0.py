class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                p1 += 1
            else:
                nums[p2] = nums[i]
                p2 += 1
        return p2