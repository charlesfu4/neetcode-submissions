class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        # generate hash map on each number's count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # now we need to reverse it -- the index of array represent the count, the number of the array represents exact number
        # might be multiple in one count
        for num, cnt in count.items():
            freq[cnt].append(num)

        # now we collect result from backward.
        # return when the result collects enough == k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
            


        