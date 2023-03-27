class Solution:
    def majorityElement(self, A, N):
        dict1,res={},0
        for item in A:
            if item in dict1:
                dict1[item]=dict1[item]+1
            else:
                dict1[item]=1
        for key in dict1:
            if dict1[key]>=res:
                res=key
        if res>N//2:
            return res
        return -1
    def majorityElements_better(self,A,N): #O(1) space complexity
        count,res=1,0
        for i in range(1,len(A)):
            if A[res]==A[i]:
                count+=1
            else:
                count-=1
            if count==0:
                count=1
                res=i
        count=0
        for item in A:
            if item==A[res]:
                count+=1
        if count>N//2:
            return A[res]
        else:
            return -1


e1=Solution()
arr=[3]
print(e1.majorityElements_better(arr,5))
