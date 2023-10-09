class Solution(object):
    def subarraySum(self, nums, k):
        l,res,currsum=0,0,nums[0]
        for r in range(len(nums)):
            if r==0:
                currsum=nums[0]
            else:
                currsum+=nums[r]
            if currsum==k:
                res+=1
            while currsum>k:
                currsum-=nums[l]
                l+=1

        return res
