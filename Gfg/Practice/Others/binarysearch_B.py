class Solution:
    def binarySearch(self,arr,n,k):
        low=0
        high=n
        while low<=high:
            print("bruh")
            mid=(low+high)//2
            if(k==arr[mid]):
                return mid+1
            elif(k>arr[mid]):
                low=mid+1
            else:
                high=mid-1
        return None
e1=Solution()
arr=[1,3,4,5,6,7,9]
print(e1.binarySearch(arr,len(arr),6))
            
