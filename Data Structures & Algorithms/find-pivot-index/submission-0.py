class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    

        def prefixSum(arr):
            prefixSum = []
            total = 0
            for n in arr:
                total += n
                prefixSum.append(total)
                
            return prefixSum
        
        ps = prefixSum(nums)

        for i in range(len(ps)):

            left_sum = 0 if i == 0 else ps[i - 1] 
            right_sum = 0 if i == len(ps) - 1 else ps[len(ps) - 1] - ps[i]

            if left_sum == right_sum:
                return i
        
        return - 1
    
                 




        