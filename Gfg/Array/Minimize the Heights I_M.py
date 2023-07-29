class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        mi,mx=arr[0],arr[0]
        ans=arr[n-1]-arr[0]
        smallest=arr[0]+k
        largest=arr[n-1]-k
        
        for i in range(n-1):
            mi=min(smallest,arr[i+1]-k)            
            mx=max(largest,arr[i]+k)
            print(mi,mx)
            if (mi<0):
                continue
            ans=min(mx-mi,ans)
        return ans
e1=Solution()
Arr = [2, 6, 3, 4, 7 ,2, 10, 3, 2, 1]
print(e1.getMinDiff(Arr,10,5))