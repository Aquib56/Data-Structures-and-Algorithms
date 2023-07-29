class Solution:
    def helper(self,adj,visited,current,res):
        visited[current]=True
        res.append(current)
        for i in range(len(adj[current])):
            if not visited[adj[current][i]]:
                self.helper(adj,visited,adj[current][i],res)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        res=[]
        visited=[False for i in range(V)]
        self.helper(adj,visited,0,res)
        return res

adj = [[2,3,1] , [0], [0,4], [0], [2]]
s=Solution()
print(s.dfsOfGraph(5,adj))
