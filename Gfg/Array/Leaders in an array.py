class Solution:
    def leaders(self, A, N):
        res=[]
        i=0
        while i<=len(A)-1:
            j=i+1
            while j<=len(A)-1 and A[i]>=A[j]:
                if j==len(A)-1:
                    res.append(A[i])
                j+=1
            i+=1
        
        res.append(A[len(A)-1])
        return res
    def optimized_Failed(self,A,N):
        i,res=0,[]
        while i<len(A)-1:
            temp=A[i+1::]
            temp.sort()
            if A[i]>=temp[len(temp)-1]:
                res.append(A[i])
            i+=1
        res.append(A[len(A)-1])
        return res
    def optimized(self,A,N):
        maxelement,res=-1,[]
        j=len(A)-1
        while j>=0:
            if maxelement<=A[j]:
                res.append(A[j])
                maxelement=A[j]
            j-=1
        res.reverse()
        return res
    
    def optimized_Failed(self,A,N):
        res,i,temp=[],0,[]
        for item in A:
            temp.append(item)
        temp.sort()
        while i<len(A)-1:
            temp.remove(A[i])
            if A[i]>=temp[len(temp)-1]:
                res.append(A[i])            
            i+=1
        res.append(A[len(A)-1])  
        return res      
    


x1=Solution()
arr=[63, 70, 80, 33, 33, 47, 20]
print(x1.optimized_Failed(arr,6))