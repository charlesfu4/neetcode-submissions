class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        window = set()
        L = 0
        window.add(nums[L])

        for R in range(1, len(nums)):
            if nums[R] not in window:
                L += 1
                nums[L] = nums[R]
                window.add(nums[R])
        
        return len(window)

