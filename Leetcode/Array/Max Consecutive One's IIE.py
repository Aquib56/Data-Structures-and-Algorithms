class Solution(object):
    def findMaxConsecutiveOnesII(self, nums):
        l,res,flag,count,idx=0,0,0,0,-1
        r=0
        while r<len(nums):
            if nums[r]==0:
                if not flag:
                    flag=1
                    idx=r
                    count+=1
                else:
                    while flag:
                        if l==idx:
                            flag=0
                            count-=1
                            r-=1
                            l+=1
                        else:
                            l+=1
                            count-=1
            else:
                count+=1
            res=max(count,res)
            r+=1
        return res
    def findMaxConsecutiveOnesII_better(self, nums):
        l, res, count, flips = 0, 0, 0, 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                flips += 1
                
            while flips > 1:
                if nums[l] == 0:
                    flips -= 1
                l += 1
                
            count = r - l + 1
            res = max(res, count)
            
        return res
                    
    
s=Solution()
test_cases = [
    [1, 1, 0, 1, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 1]
]
for item in test_cases:
    print(s.findMaxConsecutiveOnesII(item),end=" ")
    print(s.findMaxConsecutiveOnesII_better(item))