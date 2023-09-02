class Solution:  
    def isCycle(self, V,adj):
        visited=[False for i in range(V)]
        q=[[0,-1]]
        while q:
            currNode=q.pop(0)
            for i in range(len(adj[currNode[0]])):
                if visited[adj[currNode[0]][i]] and adj[currNode[0]][i]!=adj[currNode[1]]:
                    return True
                elif not visited[adj[currNode[0]][i]]:
                    visited[adj[currNode[0]][i]]=True
                    q.append([adj[currNode[0]][i],currNode[0]])
        return False

                

adj = [[], [2], [1, 3], [2]]
s=Solution()
print(s.isCycle(len(adj),adj))