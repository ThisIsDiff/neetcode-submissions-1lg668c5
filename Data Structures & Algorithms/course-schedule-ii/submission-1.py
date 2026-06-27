from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_dict = defaultdict(list)
        courses = [0 for _ in range(numCourses)]
        q = deque()
        result = []
        for course, prerequisite in prerequisites:
            courses[course] += 1
            course_dict[prerequisite].append(course)

        for i, c in enumerate(courses):
            if c == 0:
                q.append(i)

        while q:
            node = q.popleft()
            result.append(node)
            for c in course_dict[node]:
                courses[c] -= 1
                if courses[c] == 0:
                    q.append(c)

        if len(result) != numCourses:
            return []
        return result