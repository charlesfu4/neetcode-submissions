class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax = nums[0]
        lmax = 0

        gmin = nums[0]
        lmin = 0

        total = 0

        for num in nums:
            lmax = max(lmax, 0)
            lmin = min(lmin, 0)
            lmax += num
            lmin += num

            total += num

            gmax = max(gmax, lmax)
            gmin = min(gmin, lmin)
        
        if gmax > 0:
            return max(gmax, total - gmin)
        else:
            return gmax
