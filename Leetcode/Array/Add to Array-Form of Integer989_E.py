class Solution(object):
    def addToArrayForm(self, num, k):
        res=[None]*(len(num)+1)
        count=""
        total=0
        j=0
        for item in num:    
            count+=str(item)
        total=int(count)+k

        for i in str(total):
            res[j]=int(i)
            j+=1
        if j>len(num):
            return res[0:len(num)+1]
        else:
            return res[0:len(num)]
e1=Solution()
arr=[2,1,5]
print(e1.addToArrayForm(arr,806))

        
