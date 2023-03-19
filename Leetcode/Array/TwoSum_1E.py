class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(nums[i]+nums[j]==target and i!=j):
                    return i,j

class Solutions(object):
    def TwoSum(self, nums, target):
        if len(nums)<0:
            return False
        dict1={}
        
        for i in range(0,len(nums)):
            if nums[i] in dict1:
                return dict1[nums[i]]+1,i+1
            else:
                dict1[target-nums[i]]=i    
       



if __name__=="__main__":
    arr=[-1,1,2,-1,0]
    e1=Solutions()
    print(e1.TwoSum(arr,-1))

