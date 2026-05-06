class Stack:
    def __init__(self):
        self.arr = []
    
    def pop(self) -> str:
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return None
    
    def push(self, val: str):
        self.arr.append(val)
    
    def peek(self) -> str:
        if len(self.arr) > 0:
            return self.arr[len(self.arr) - 1]
        else:
            return None
    
    def len(self) -> int:
        return len(self.arr)

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        char_stk = Stack()

        i = 0

        while i < len(s):
            if s[i] in ['(', '[', '{']:
                char_stk.push(s[i])
                i += 1
            elif s[i] in [')', ']', '}']:
                top = char_stk.peek()
                if (top == '(' and s[i] == ')') or (top == '[' and s[i] == ']') or (top == '{' and s[i] == '}'):
                    char_stk.pop()
                    i += 1
                else:
                    return False
        
        
        return char_stk.len() == 0 
            

        