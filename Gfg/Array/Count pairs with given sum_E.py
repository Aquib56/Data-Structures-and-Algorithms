class Solution:
    def getPairsCount(self, arr,k):
        res=[]
        for i in range(len(arr)):
            diff=(k-arr[i])
            print(diff)
            j=i+1
            while j<=len(arr)-1:
                if arr[j]==diff:
                    res.append([i,j])
                j+=1
            
        return res
    def getPairsCount_better(self,arr,k):
        dict1={}
        count=0
        for i in range(len(arr)):
            diff=k-arr[i]
            if arr[i] in dict1:
                count+=dict1[arr[i]]
            if diff in dict1:
                dict1[diff]=dict1[diff]+1
            else:
                dict1[diff]=1
        return count

e1=Solution()
arr=[1 ,5 ,5 ,5, 5, 7]
print(e1.getPairsCount_better(arr,10))