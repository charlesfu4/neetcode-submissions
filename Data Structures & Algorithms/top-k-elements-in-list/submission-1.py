class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)

        for i in range(len(nums)):
            hmap[nums[i]] += 1
        
        buckets = [[] for i in range(len(nums) + 1)] # len + 1 to cover the max freq than can occur, eg. 4 element arrary need index len(arr)
        for key, val in hmap.items():
            buckets[val].append(key)

        
        res = []

        for i in range(len(buckets) - 1, 0, -1): # go down from the highest freq to collect each key
            for key in buckets[i]:
                res.append(key)
                if len(res) == k: # always return if the append met the final condition
                    return res

            




        