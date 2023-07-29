from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q=[0]
        res=[]
        visited=[False for i in range(V)]
        while q:
            node=q.pop(0)
            if node not in res:
                res.append(node)
            visited[node]=True
            for i in range(len(adj[node])):
                if not visited[adj[node][i]]:
                    q.append(adj[node][i])
        return res
adj = [[1, 2, 4, 8] , [0, 5, 6, 9], [0,4], [7, 8],[0, 2],[1, 8],[1, 7, 9],[3, 6],[0, 3, 5] ,[1, 6]]
s=Solution()
print(s.bfsOfGraph(10,adj))