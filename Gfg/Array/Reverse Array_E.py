class Solutions:
    def swap(self,nums):
        l,r=0,len(nums)-1
        while l!=r:
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
            r-=1
            l+=1
        return nums
    def recursiveSwap(self,nums,l,r):
        if l==r:
            print(nums)
            return
        temp=nums[r]
        nums[r]=nums[l]
        nums[l]=temp
        self.recursiveSwap(nums,l+1,r-1)
s=Solutions()
nums=[5,1,5,6,2]
print(s.recursiveSwap(nums,0,len(nums)-1))