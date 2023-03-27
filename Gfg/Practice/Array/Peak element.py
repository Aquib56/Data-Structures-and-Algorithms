class Solution:   
    def peakElement(self,arr):
        i=1
        if len(arr)==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[len(arr)-1]>arr[len(arr)-2]:
            return len(arr)-1
        while i+1<=len(arr)-1:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return i
            i+=1
        return -1
arr = [1,2,1,3]
e1=Solution()
print(e1.peakElement(arr))