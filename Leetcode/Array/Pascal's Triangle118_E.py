class Solution(object):
    def helper(self,nums):
        res=[]
        for i in range(len(nums)-1):
            res.append(nums[i]+nums[i+1])
        res=[1]+res +[1]
        return res
    def generate(self, numRows):
        res=[]
        row=1
        if row==1:
            res.append([1])
            row+=1
        if row==2:
            res.append([1,1])
            row+=1
        while numRows-row>=0:
            res.append(self.helper(res[row-2]))
            row+=1
        return res

s=Solution()
print(s.generate(5))
            
            