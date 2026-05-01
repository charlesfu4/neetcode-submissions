class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_counter = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                if counter > max_counter:
                    max_counter = counter
            else:
                if counter > max_counter:
                    max_counter = counter
                counter = 0
        
        return max_counter
        