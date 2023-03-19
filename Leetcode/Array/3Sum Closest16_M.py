class Solution(object):
    def threeSumClosest(self, nums, target):
        res=[1341341]
        threesum,prev=0,0
        nums.sort()
        for idx,item in enumerate(nums):
            l,r=idx+1,len(nums)-1
            while l<r and abs(((target)-(prev))<=abs((target)-(threesum))):
                threesum=nums[l]+nums[r]+item
                if threesum>target:
                    r-=1
                elif threesum<target:
                    l+=1
                prev=threesum
            if abs(((target)-(prev))<=abs((target)-(res[0]))):
                res[0]=prev
        return res
    def better(self,nums,target):
        ans=0
        diff=float("inf")
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                currentsum=nums[left]+nums[right]+nums[i]
                if currentsum==target:
                    return target
                if abs(currentsum-target)<abs(diff-target):
                    diff=currentsum
                    ans=currentsum
                if currentsum>target:right-=1
                if currentsum<target:left+=1
        return ans
    def threeSumClosest_best(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum
                    
                


             
x1=Solution()
nums=[-1,2,1,-4]
print(x1.better(nums,1))            
