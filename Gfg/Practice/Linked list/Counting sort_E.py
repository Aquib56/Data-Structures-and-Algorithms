class Solution:
    def countSort(self,arr):
        count=[0]*26
        res=""
        for item in arr:
            idx=ord(item)-97
            count[idx]+=1
        for i in range(len(count)):
            while count[i]!=0:
                res+=(chr(i+97))
                count[i]-=1
        return res
s=Solution()
print(s.countSort("cba"))