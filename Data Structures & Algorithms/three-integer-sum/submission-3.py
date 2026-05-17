class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
                
            r = len(nums) - 1
            l = i + 1

            while l < r:
                if nums[i] + nums[l] < -nums[r]:
                    l += 1
                elif nums[i] + nums[l] > -nums[r]:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                


    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     count = defaultdict(int)
    #     for num in nums:
    #         count[num] += 1
        
    #     res = []
    #     for i in range(len(nums)):
    #         count[nums[i]] -= 1
    #         # no duplicate triple
    #         if i and nums[i] == nums[i-1]:
    #             continue
    #         for j in range(i + 1, len(nums)):
    #             count[nums[j]] -= 1
    #             # no duplicate triple
    #             if j - 1 > i and nums[j] == nums[j - 1]:
    #                 continue

    #             target = -(nums[i] + nums[j])
    #             if count[target] > 0:
    #                 res.append([nums[i], nums[j], target])
            
    #         # number can be reused
    #         for j in range(i + 1, len(nums)):
    #             count[nums[j]] += 1
        
    #     return res
            

        