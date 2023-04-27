class Solution:
    def subArraySum(self,arr, n, s): 
        i=0
        res=0
        for r in range(n):
            res=0
            while(res<s):
                if(r>n-1):
                    break
                else:
                    res=res+arr[r]
                    r=r+1
            i+=1
            if res==s:
                return i,r
        return -1
    def subArraySum2(self,arr, n, s): 
        l,r,currsum=0,0,0
        while r<=n:
            print(currsum,l,r)
            if currsum<s:
                currsum=currsum+arr[r]
                r+=1
            elif currsum>s:
                currsum=currsum-arr[l]
                l+=1
            else:
                return l+1,r
        currsum+=arr[n-1]
        if currsum==s:
            return l+1,r            
        return -1,-1
    
if __name__=="__main__":
    e1=Solution()
    arr=[135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
    print(e1.subArraySum2(arr,len(arr),468))
