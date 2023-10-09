class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visitSet=set()
        def dfs(crs):
            if crs in visitSet:return False
            if preMap[crs]==[]:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):return False
            visitSet.remove(crs)
            preMap[crs]=[]
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):return False
        return True
class Solution(object):
    def cycle(self,g,visited,rec,curr):
        visited[curr]=True
        rec[curr]=True
        for i in range(len(g[curr])):
            print(g[curr])
            if rec[g[curr][i][1]]:
                return True
            if not visited[g[curr][i][1]]:
                if self.cycle(g,visited,rec,g[curr][i][1]):
                    return True
        rec[curr]=False
        return False
    def canFinish(self, numCourses, prerequisites):
        g=[[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            g[prerequisites[i][0]].append([prerequisites[i][0],prerequisites[i][1]])
        visited=[False for i in range(numCourses)]
        rec=[False for i in range(numCourses)]
        for i in range(numCourses):
            if self.cycle(g,visited,rec,i):
                return False
        return True

            
            

        
        


            
            

        