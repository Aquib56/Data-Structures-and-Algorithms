class Solution(object):
    def canJump(self, nums):
        i,jumps,count,prev=0,0,len(nums),-1
        while i<len(nums)-1:
            i+=nums[i]
            jumps+=1
            if prev==i:
                return False
            prev=i
        return True
e1=Solution()
arr=[2,5,0,0]
print(e1.canJump(arr))