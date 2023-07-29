class Solution:
    def helper(self,adj,visited,rec,curr):
        visited[curr]=True
        rec[curr]=True
        for i in range(len(adj[curr])):
            if rec[adj[curr][i]]:
                return True
            elif not visited[adj[curr][i]]:
                if self.helper(adj,visited,rec,curr):
                    return True
        rec[curr]=False
        return False
                
            
    def isCycle(self, V,adj):
            visited=[False]*V
            rec=[False]*V
            return self.helper(adj,visited,rec,0)
s=Solution()
adj = [[], [0, 2, ],[1, 3], [2, 4],[1, 3]]
print(s.isCycle(len(adj),adj))