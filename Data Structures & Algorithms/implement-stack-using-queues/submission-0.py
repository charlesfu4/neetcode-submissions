
class MyStack:

    def __init__(self):
        self.q = deque()
        self.counter = 0
        self.last_ele = None
        

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        self.counter += 1


    def pop(self) -> int:
        self.counter -= 1
        x = self.q.popleft()
        return x
        
        

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.counter == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
