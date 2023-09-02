class Solution(object):
    def longestOnes(self, nums, k):
        flips,l,res=0,0,0
        for r in range(len(nums)):
            if nums[r]==0:
                flips+=1
            while flips>k:
                if nums[l]==0:
                    flips-=1
                l+=1
            res=max(res,r-l+1)
        return res
            