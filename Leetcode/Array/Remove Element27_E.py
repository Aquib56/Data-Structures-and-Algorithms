class Solution(object):
    def removeElement(self, nums, val):
        i=0
        total=len(nums)
        j=len(nums)-1
        while(i<=len(nums)-1):
            if(nums[i]==val):
                if(j<0):
                    nums[i]=0
                    total=total-1
                elif(nums[j]==val):
                    j=j-1
                else:
                    nums[i]=nums[j]
                    j=j-1
                    total=total-1
            else:
                i=i+1
        return total
    def Ezmethod(self,nums,val):
        count=0
        for i in range(0,len(nums)):
            if(nums[i]!=val):
                nums[count]=nums[i]
                count+=1
        return count,nums

if __name__=="__main__":
    height = [2,3,3,2]
    e1=Solution()
    print(e1.Ezmethod(height,3))
