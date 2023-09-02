class Solution(object):
    def findMaxConsecutiveOnesII(self, nums):
        l,res,flag,count,idx=0,0,0,0,-1
        r=0
        while r<len(nums):
            if nums[r]==0:
                if not flag:
                    flag=1
                    idx=r
                    count+=1
                else:
                    while flag:
                        if l==idx:
                            flag=0
                            count-=1
                            r-=1
                            l+=1
                        else:
                            l+=1
                            count-=1
            else:
                count+=1
            res=max(count,res)
            r+=1
        return res