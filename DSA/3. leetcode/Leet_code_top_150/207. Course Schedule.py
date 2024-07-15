class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pm = { i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pm[crs].append(pre)
        vSet = set()
        def dfs(crs):
            if crs in vSet:
                return False
            if pm[crs] == []:
                return True
            
            vSet.add(crs)
            for pre in pm[crs]:
                if not dfs(pre): return False
            vSet.remove(crs)
            pm[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
