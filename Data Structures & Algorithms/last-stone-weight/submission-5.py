class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        def percolation(arr, i):
            # while there are left child
            while 2 * i < len(arr): 
                # check if right child exists, and larger then left plus larger then the parent
                # -> percolate down if true
                if 2*i + 1 < len(arr) and arr[2*i + 1] > arr[2*i] and arr[i] < arr[2*i + 1]:
                    tmp = arr[i]
                    arr[i] = arr[2*i + 1]
                    arr[2*i + 1] = tmp
                    i = 2*i + 1
                # otherwise check if the left larger then the parent
                # -> percolate down if true
                elif arr[i] < arr[2*i]:
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

            percolation(arr, i)

            return res
        
        def push(arr, ele):
            # append at the end of the array
            arr.append(ele)
            # get the index of the element
            i = len(arr) - 1

            # while the index > 1(means there are parent and child)
            # we need to check percolate up
            # if the child is larger then the parent
            while i > 1 and arr[i] > arr[i//2]:
                tmp = arr[i]
                arr[i] = arr[i//2]
                arr[i//2] = tmp
                i = i // 2


        # Step 1: heapilfy

        # append the first element to end of array
        # and make the first element dummy
        stones.append(stones[0])

        # we only need to check percolation from the last parent upward
        curr = (len(stones) - 1)// 2

        # assign the pointer for the last parent

        while curr > 0:
            # assign another i for the inner while loop
            i = curr
            # percolation
            percolation(stones, i)
            # here we have to backup 1 position everytime the percolation check is done
            curr -= 1
        
        # Step 2a: Popping 2 largest

        # After this the array is heaplify
        # we should start poping recursively

        while len(stones) > 2:
            print(stones)
            first = pop(stones)
            second = pop(stones)
            diff = first - second
            # Step 2b: push this diff back to the heap
            if diff > 0:
                push(stones, diff)
            
        if len(stones) == 1:
            return 0
        else:
            return stones[1]
        





            

        
        