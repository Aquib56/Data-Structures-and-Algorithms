class Solution(object):
    def threeSum(self, nums):
        res=[]
        nums.sort()
        for idx,item in enumerate(nums):
            if idx>0 and item==nums[idx-1]:
                continue
            l,r=idx+1,len(nums)-1
            while l<r:
                threesum=item+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([item,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
    def sum3(self,nums):
        res=[]
        nums.sort()
        for idx,item in enumerate(nums):
            if idx>0 and item==nums[idx-1]:
                continue
            l,r=idx+1,len(nums)-1
            while l<r:
                threesum=item+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([item,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
if __name__=="__main__":
    arr=[-4,-1,-1,0,1,2]
    e1=Solution()
    print(e1.sum3(arr))