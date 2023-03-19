class Solution(object):
    def searchInsert(self, nums, target):
        i=0
        while(i<len(nums)):
            if(nums[i]==target):
                return i
            elif(nums[i]>target):
                return i
            else:
                i+=1
        return i
    def BinarySearchMethod(self,nums,target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=round(low+(high-low)/2)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                high=mid-1
            else:
                low=mid+1
        return low
if __name__=="__main__":
    arr=[1,3,5,6,8]
    e1=Solution()
    print(e1.BinarySearchMethod(arr,3))