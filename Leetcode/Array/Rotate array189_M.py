class Solution(object):
    def rotate(self, nums, k):
        res=[0]*len(nums)
        for i in range(len(nums)):
            position=(i+k)%len(nums)
            res[position]=nums[i]
        for i in range(len(nums)):
            nums[i]=res[i]
nums=[1,2]
s=Solution()
print(s.rotate(nums,5))