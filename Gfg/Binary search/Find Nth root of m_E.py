
def NthRoot(n, m):
        low,high=1,m
        while low<=high:
            mid=(low+high)//2
            print(mid**n,mid)
            if mid**n==m:
                return mid
            elif mid**n>m:
                high=mid-1
            else:
                low=mid+1
        return -1
        
print(NthRoot(2,9))