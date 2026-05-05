class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def percolate(arr, i):
            while 2*i < len(arr):
                if 2*i + 1 < len(arr) and arr[2*i+1] > arr[2*i] and arr[2*i+1] > arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[2*i+1]
                    arr[2*i+1] = tmp
                    i = 2*i+1
                elif arr[2*i] > arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[2*i]
                    arr[2*i] = tmp
                    i = 2*i
                else:
                    break
        
        def pop(arr):
            if len(arr) == 1:
                return None
            if len(arr) == 2:
                return arr.pop()
            
            
            res = arr[1]

            arr[1] = arr.pop()

            i = 1

            percolate(arr, i)
            return res

        
        def heapify(arr):
            arr.append(arr[0])

            curr = (len(arr) - 1) // 2

            while curr > 0:
                i = curr

                percolate(arr, i)

                curr -= 1
            
            return arr
        
        heap_arr = heapify(nums)

        for i in range(k-1):
            pop(heap_arr)
        return pop(heap_arr)


        




            

        