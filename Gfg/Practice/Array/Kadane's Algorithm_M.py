class Solution:
    def maxSubArraySum(self,arr,N):
        l,sum,prevsum,res=0,0,0,0

        for r in range(len(arr)):
            sum+=arr[r]
            print(sum,prevsum)
            if prevsum>sum:
                sum=sum-arr[l]
                l+=1    
            prevsum=sum
            res=max(res,sum) 
        return res
    def better(self,arr):   
        maxSum=arr[0]
        currSum=0
        for n in arr:
            if currSum<0:
                currSum=0
            currSum+=n
            maxSum=max(maxSum,currSum)
        return maxSum


                
e1=Solution()
arr=[1,2,-3,5]
print(e1.better(arr))