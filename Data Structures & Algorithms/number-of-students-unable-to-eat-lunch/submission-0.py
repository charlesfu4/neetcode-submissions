
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cp = 0
        sp = 0
        for i in range(len(students)):
            if students[i] == 1:
                sp += 1
            elif students[i] == 0:
                cp += 1
        
        remain = len(students)

        for sw in sandwiches:
            if sw == 1 and sp > 0:
                sp -= 1
                remain -= 1
            elif sw == 0 and cp > 0:
                cp -= 1
                remain -= 1
            else:
                break
        return remain
        


