class Solution:
    def MissingNumber(self,array,n):
        array.sort()
        i=0
        while i+1<len(array) and array[i]+1==array[i+1]:
            i+=1
        if array[0]!=1:
            return 1
        else:
            return array[i]+1

e1=Solution()
arr=[2]
print(e1.MissingNumber(arr,5))