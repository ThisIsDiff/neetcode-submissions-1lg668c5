class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
            
        prereq = defaultdict(list)
        for course, prerequisite in prerequisites:
            prereq[course].append(prerequisite)
        visited = set()

        def dfs(num):
            if num in visited:
                return False
            if prereq[num] == []:
                return True 

            visited.add(num)
            for pre in prereq[num]:
                if not dfs(pre):
                    return False
            visited.remove(num)
            prereq[num]= []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False

        return True