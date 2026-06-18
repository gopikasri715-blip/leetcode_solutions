from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for c, pre in prerequisites:
            graph[c].append(pre)

        visit = set()
        path = set()

        def dfs(course):
            if course in path:
                return False

            if course in visit:
                return True

            path.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            path.remove(course)
            visit.add(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True