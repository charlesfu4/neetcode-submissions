class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # store each element from the array in a hash map 
        hmap = {}
        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = [i]
            else:
                hmap[nums[i]].append(i) 
        
        # loop through the hashmap and seach for the diff

        print(hmap)

        for i, key in enumerate(hmap.keys()):
            diff = target - key
            if diff in hmap:
                if diff == key:
                    if len(hmap[diff]) != 1:
                        return hmap[diff]
                    else:
                        continue
                else:
                    j = hmap[diff][0]
                    print(j)
                    if i > j:
                        return [j, i]
                    else:
                        return [i, j]


        