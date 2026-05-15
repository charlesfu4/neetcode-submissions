class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while l <= r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m

            # check which half is still sorted
            if nums[m] <= nums[r]: # right half sorted
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r =  m - 1
            else: # left half sorted
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1


        return - 1
