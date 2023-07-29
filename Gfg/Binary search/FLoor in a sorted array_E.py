class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        diff=float("inf")
        curr=1
        i=0
        res=-1
        while i<=N-1 and curr>=0:
            curr=X-A[i]
            if curr<=diff and curr>=0:
                diff=curr
                res=i
            i+=1
        return res
    
    def findFloor1(self,A,N,X):
        low=0
        high=N-1
        while low<=high:
            mid=(low + high)//2
            print(mid,low,high,X,A[mid],X-A[mid])
            if X-A[mid]==0:
                return mid
            elif X-A[mid]<0:
                high=mid-1
            else:
                low=mid+1
        return -1
    def BS(self,A,x):
        low=0
        high=len(A)-1
        while low<=high:
            mid=(low + high)//2
            if A[mid]==x:
                return mid
            elif A[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return -1

                
s=Solution()
a=[1,2,8,10,11,12,19]
print(s.findFloor(a,len(a),20))