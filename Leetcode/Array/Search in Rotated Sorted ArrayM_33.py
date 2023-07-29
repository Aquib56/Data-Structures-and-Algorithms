class Solution(object):
    def search(self, nums, target):
        left,right=0,len(nums)-1
        mid=(left+right)//2
        while left <= right:
            mid=(left+right)//2
            print(nums[mid])
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if target>nums[mid] or target <nums[left]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if target<nums[mid] or target >nums[right]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
                
if __name__=="__main__":
    nums = [1,3]
s1=Solution()
print(s1.search(nums,3))