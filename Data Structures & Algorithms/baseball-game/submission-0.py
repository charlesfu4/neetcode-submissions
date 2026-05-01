class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        p = -1

        for i in range(len(operations)):
            if operations[i] == "+":
                print(scores)
                scores.append(int(scores[p]) + int(scores[p - 1]))
                p += 1
            elif operations[i] == "C":
                scores.pop()
                p -= 1

            elif operations[i] == "D":
                scores.append(int(scores[p]) * 2)
                p += 1
            else:
                scores.append(int(operations[i]))
                p += 1
                print(scores)

        return sum(scores)
        