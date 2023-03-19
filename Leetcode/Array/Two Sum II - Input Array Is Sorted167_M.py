class Solution(object):
    def twoSum(self, nums, target):
        res=[]
        if len(nums)<0:
            return False
        dict1={}
        
        for i in range(0,len(nums)):
            if nums[i] in dict1:
                 res.append(dict1[nums[i]]+1)
                 res.append(i+1)
                 return res
            else:
                dict1[target-nums[i]]=i    
    def method2(self,nums,target):
        res=[]
        for i in range(len(nums)):
            diff=target-nums[i]
            j=i+1
            while j<len(nums) and nums[j]<=diff:
                # print(nums[j],target)
                if nums[j]==diff:
                    res.append(i+1)
                    res.append(j+1)
                    return res
                j+=1

if __name__=="__main__":
    arr=[2,7,11,15]
    e1=Solution()
    print(e1.method2(arr,9))