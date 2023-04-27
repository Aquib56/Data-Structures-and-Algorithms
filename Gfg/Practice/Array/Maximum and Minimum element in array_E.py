class Solution:
    def findSum(self,A,N): 
        if len(A)==1:
            return A[0],A[0]
        if len(A)==2:
            if A[0]>A[1]:
                return A[1],A[0]
            else:
                return A[0],A[1]
        else:
            return(self.findSum(A[:len(A)//2]),self.findSum(A[len(A)//2:len(A)]))
            
    
