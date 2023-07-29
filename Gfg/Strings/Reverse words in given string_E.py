class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        i=0
        arr=[]
        temp=""
        res=""
        for item in S:
            if item==".":
                arr.append(temp)
                temp=""
            else:
                temp+=item
        arr.append(temp)
        i=len(arr)-1
        while i>0:
            res+=arr[i]
            res+="."
            i-=1
        res+=arr[0]
        return res
res="ab"
res