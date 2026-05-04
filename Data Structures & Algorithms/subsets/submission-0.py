class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(2**len(nums)):
            ar = []
            for j in range(len(nums)):
                if i & (1 << j):
                    ar.append(nums[j])
            arr.append(ar)
        
        return  arr
        
        



        