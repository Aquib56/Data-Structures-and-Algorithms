class Solution:
    def sort012(self,arr,n):
        res,zero,one,two=[],[],[],[]
        for item in arr:
            if item==0:
                zero.append(0)
            elif item==1:
                one.append(1)
            else:
                two.append(2)
        res=zero+one+two
        return res
    def sort012_better(self,arr,n):
        low,mid,high,temp=0,0,len(arr)-1,-2
        while mid<=high-1:
            if arr[mid]==0:
                temp=arr[low]
                arr[low]=arr[mid]
                arr[mid]=temp
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                temp=arr[high]
                arr[high]=arr[mid]
                arr[mid]=temp
                high=-1
        return arr
s1=Solution()
arr= [0 ,2, 1, 2, 0,1,1,1]
print(s1.sort012_better(arr,5))