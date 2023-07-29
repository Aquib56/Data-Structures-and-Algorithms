class Solution:
    def nextLargerElement(self,arr,n):
        result=[]
        i=0
        while(i<len(arr)-1):
            for j in range(i,len(arr)):
                if(arr[i]<arr[j]):
                    result.append(arr[j])
                    bol=True
                    break
                else:
                    bol=False
            if(bol==False):
                result.append(-1)
            i+=1
        result.append(-1)
        return result
if __name__=="__main__":
    e1=Solution()
    arr=[6,8,0,1,3]
    print(e1.nextLargerElement(arr,4))    