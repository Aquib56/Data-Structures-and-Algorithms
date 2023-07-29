class Solution:
    def allPairs(self, A, B, X):
        res=[]
        diff={}
        for item in A:
            diff[item]=X-item
        for key in diff.keys():
            if diff[key] in B:
                res.append([key,diff[key]])
        return res
s=Solution()
A=[-1, -2, 4, -6, 5, ]
B= [6, 3, 4, 0]
b=(s.allPairs(A,B,8))
b.sort()
print(b)