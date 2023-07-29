class Solution:
    def duplicates(self, arr, n): 
        res=[]
        i=0
        arr.sort()
        while i<=len(arr)-2 :
            if arr[i]==arr[i+1]:
                if arr[i] not in res:       
                    res.append(arr[i])
            i+=1
        if not res:
            res.append(-1)
            return res
        else:
            return res
    def set1(self,arr,n):
        s=set()
        for item in arr:
            s.add(item)
        
        # z=s.difference(set(arr))
        a=set(arr)
        print(a)
x1=Solution()
arr=[5,3,5,6]
print(x1.set1(arr,5))