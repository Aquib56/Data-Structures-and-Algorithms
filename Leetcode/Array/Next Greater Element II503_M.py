class Solution(object):
    def nextGreaterElements(self, nums):
        n=len(nums)
        res=[-1]*n
        stack=[]
        for i in range(2*n):
            curr=nums[i%n]
            while stack and curr>nums[stack[-1]]:
                element=stack.pop()
                res[element]=curr
            if i<n:
                stack.append(i)
        return res
                    

s=Solution()
nums = [1,2,1]
print(s.nextGreaterElements(nums))                  
                
            
                

                