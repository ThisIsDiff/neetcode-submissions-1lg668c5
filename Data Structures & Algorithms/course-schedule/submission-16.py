from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dictionary = defaultdict(set)
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            indegree[prerequisite] += 1
            course_dictionary[course].add(prerequisite)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)


        finished_course = 0
        while q:
            c = q.popleft()
            finished_course += 1  
            for course in course_dictionary[c]:
                indegree[course] -= 1 
                if indegree[course] == 0:
                    q.append(course)         
        
        return finished_course == numCourses