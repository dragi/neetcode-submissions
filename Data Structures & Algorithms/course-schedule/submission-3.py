class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereq = {i:[] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            courseToPrereq[course].append(prereq)

        def dfs(course, visited):
            if course in visited:
                return False
            visited.add(course)
            
            if len(courseToPrereq[course]) > 0:
                for prereq in courseToPrereq[course]:
                    if dfs(prereq, visited):
                        courseToPrereq[course].remove(prereq)
                        return True
                    else:
                        return False
            return True

        for i in range(numCourses):
            visited = set()
            if not dfs(i, visited):
                return False

        return True