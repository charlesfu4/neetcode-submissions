class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0]
        nums_length = len(nums)

        # add counts to each bucket
        for i in range(nums_length):
            counts[nums[i]] += 1

        # loop through each bucket to releases counts
        k = 0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[k] = i
                k += 1
        


        