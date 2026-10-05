class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = { i:[] for i in range(numCourses)}
        visited = set()

        for prereq, course in prerequisites:
            courseToPrereq[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False
            if len(courseToPrereq[course]) == 0:
                return True
            visited.add(course)
        
            for prereq in courseToPrereq[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            courseToPrereq[course] = []
            return True

        for i in range(numCourses):
            visited = set()
            if not dfs(i):
                return False
        return True