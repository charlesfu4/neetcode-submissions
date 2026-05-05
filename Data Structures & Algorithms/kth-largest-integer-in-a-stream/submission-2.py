class KthLargest:
    def __init__(self, k: int, nums: List[int]):

        self.nums = [0]
        self.k = k
        for i in range(len(nums)):
            self.push(nums[i])

    def push(self, ele):
        self.nums.append(ele)
        i = len(self.nums) - 1

        while i > 1 and self.nums[i] < self.nums[i//2]:
            tmp = self.nums[i]
            self.nums[i] = self.nums[i // 2]
            self.nums[i // 2] = tmp
            i = i // 2
        print(self.nums)
    
    def pop(self):
        if len(self.nums) == 1:
            return None
        if len(self.nums) == 2:
            return self.nums.pop()
    
        res = self.nums[1]   
        # Move last value to root
        self.nums[1] = self.nums.pop()
        i = 1
        # Percolate down
        while 2 * i < len(self.nums):
            if (2 * i + 1) < len(self.nums) and self.nums[2 * i + 1] < self.nums[2 * i] and self.nums[i] > self.nums[2 * i + 1]:
                # Swap right child
                tmp = self.nums[i]
                self.nums[i] = self.nums[2 * i + 1]
                self.nums[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.nums[i] > self.nums[2 * i]:
                # Swap left child
                tmp = self.nums[i]
                self.nums[i] = self.nums[2 * i]
                self.nums[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res




    def add(self, val: int) -> int:
        self.push(val)

        while len(self.nums) > (self.k + 1):
            self.pop()

        # pop len(self.nums) - k times to keep the kth element on the top of the heap
        return self.nums[1]

        
