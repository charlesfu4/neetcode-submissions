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
        # boundary case while there is only 1 char
        if len(s) <= 1:
            return False
        
        # Now create a stack for the left-sided chars
        char_stk = Stack()

        # assign pointer that we can walk through all chars
        i = 0
        while i < len(s):
            # push left-sided chars into stack, increment the pointer after that
            if s[i] in ['(', '[', '{']:
                char_stk.push(s[i])
                i += 1
            # if encounter right-sided chars
            # check if the top element matches as a pair
            elif s[i] in [')', ']', '}']:
                top = char_stk.peek()
                # match then pop the left-sided char from the stack and increment the pointer after that
                if (top == '(' and s[i] == ')') or (top == '[' and s[i] == ']') or (top == '{' and s[i] == '}'):
                    char_stk.pop()
                    i += 1
                # if not - immediately exit with False
                else:
                    return False
        # lastly, we check if all the left-sided chars are consumed up
        # since the only early exit is non-matched right side char
        # only possibility is that the right side chars all matched but are not enough to use up the left-sided chars sitting in the stack
        return char_stk.len() == 0 
            

        