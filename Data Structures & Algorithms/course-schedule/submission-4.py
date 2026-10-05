class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereqs = {i:[] for i in range(numCourses)}
        visited = set()

        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)

        def dfs(course):
            if course in visited:
                return False
            if courseToPrereqs[course] == []:
                return True
            visited.add(course)

            for prereq in courseToPrereqs[course]:
                if not dfs(prereq):
                    return False
                
            courseToPrereqs[course] = []
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True