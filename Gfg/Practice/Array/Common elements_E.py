class Solution:
    def commonElements (self,A, B, C):
        i,j,k,res=0,0,0,[]
        dict1={}
        while i<=len(A)-1 and j<=len(B)-1 and k<len(C)-1:
            if A[i]==B[j]==C[k]:
                dict1[A[i]]=+1
                res.append(A[i])
                i+=1
                j+=1
                k+=1
            else:
                if A[i]<B[j] and A[i]<C[k]:
                    i+=1   
                elif B[j]<A[i] and B[j]<C[k]:
                    j+=1
                elif C[k]<A[i] and C[k]<B[j]:
                    k+=1
        return res         
e1=Solution()
A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
print(e1.commonElements(A,B,C))    