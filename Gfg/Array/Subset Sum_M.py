class Solution:
    def subsetSums(self, arr, N):
        res=[]
        def helper(index,sum):
            if index==N:
                res.append(sum)
                return
            helper(index+1,sum+arr[index])
            helper(index+1,sum)
        helper(0,0)
        res.sort()
        return res


s=Solution()
a=[2,3]
print(s.subsetSums(a,2))