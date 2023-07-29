import math
class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort()
        count=0
        for i in range(n-2):
            left=n-2
            right=n-1
            diff=sumo-arr[i]            
            permute=n-(i+1)
            while arr[left]+arr[right]>=diff and left>i:
                left-=1
                right-=1
                permute-=1
            print(arr[i],arr[left],arr[right],permute)
            p=math.comb(permute,2)
            count+=p
        return count
s1=Solution()
nums= [1,3,4,5,7]
print(s1.countTriplets(nums,len(nums),12))