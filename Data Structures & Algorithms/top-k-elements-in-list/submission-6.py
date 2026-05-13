class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = defaultdict(int)

        for i in range(len(nums)):
            hmap[nums[i]] += 1
        


        heap = []

        for key, val in hmap.items():
            heapq.heappush(heap , (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        


        