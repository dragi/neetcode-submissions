class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courseToPrereq[course].append(prereq)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            if courseToPrereq[course] == []:
                return True
            
            seen.add(course)
            for prereq in courseToPrereq[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            courseToPrereq[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True