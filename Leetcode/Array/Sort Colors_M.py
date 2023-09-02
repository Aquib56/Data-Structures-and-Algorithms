class Solution(object):
    def sortColors(self, nums):
        zero,one,two=0,0,0
        for item in nums:
            if item==0:
                zero+=1
            elif item==1:
                one+=1
            else:
                two+=1
        i=0
        while zero:
            nums[i]=0
            i+=1
            zero-=1
        while one:
            nums[i]=1
            i+=1
            one-=1
        while two:
            nums[i]=2
            i+=1
            two-=1
        return nums
    def sortColors_better(self, nums):
        l,r,i=0,len(nums)-1,0
        while i<=r:
            if nums[i]==0:
                nums[i],nums[l]=nums[l],nums[i]
                i+=1
                l+=1
            if nums[i]==2:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
            else:
                i+=1
            print(nums)
        return nums
            

        
s=Solution()
nums=[2,0,1]
print(s.sortColors_better(nums))