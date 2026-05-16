class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ["+", "-", "*", "/"]
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i])) 
            else:
                num2 = stack.pop()
                res = stack.pop()
                if tokens[i] == '+':
                    res += num2
                elif tokens[i] == '-':
                    res -= num2
                elif tokens[i] == '*':
                    res *= num2
                elif tokens[i] == '/':
                    res = int(res/ num2)
                stack.append(res)



        return res
        