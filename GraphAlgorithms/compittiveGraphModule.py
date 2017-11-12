"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        dict = {}
        for e in employees:
            dict[e.id] = e
        print(dict)

        visited = [False] * (len(employees) + 1)
        que = []
        que.append(dict[id])
        sum = 0
        while (que):
            emp = que.pop()
            sum += emp.importance
            visited[emp.id] = True

            for i in range(len(emp.subordinates)):
                if visited[i] == False:
                    que.append(dict[i])

        return sum


c = Solution()
c.getImportance([[1, 2, [2]], [2, 3, []]], 1)
