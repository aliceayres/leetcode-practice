"""
690. Employee Importance
You are given a data structure of employee information, which includes the employee's unique id,
his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3.
They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure
ike [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []].
Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.
Now given the employee information of a company, and an employee id, you need to return the total
importance value of this employee and all his subordinates.
Example 1:
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:
One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.
"""

# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        cache = {}
        for em in employees:
            cache[em.id] = em
        importance = 0
        stack = []
        stack.append(id)
        while len(stack) > 0:
            current_id = stack.pop(-1)
            current = cache.get(current_id, None)
            if current != None:
                importance += current.importance
                for sub_id in current.subordinates:
                    stack.append(sub_id)
        return importance

if __name__ == '__main__':
    slt = Solution()
    input = [[1,2,[2,3]], [2,3,[4]],[3,5,[]],[4,10,[]]] # employees not have loop relationship
    id = 1
    emps = [Employee(x[0],x[1],x[2]) for x in input]
    print(slt.getImportance(emps,id))