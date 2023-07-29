class Solution(object):
    def reverseWords(self, s):
        i=0
        arr=[]
        temp=""
        res=""
        prev=" "
        for item in s:
            if item==" " and prev==" ":
                continue
            elif item==" ":
                arr.append(temp)
                temp=""
            else:
                temp+=item
            prev=item
        arr.append(temp)
        i=len(arr)-1
        while i>0:
            res+=arr[i]
            res+=" "
            i-=1
        res+=arr[0]
        new_string=""
        if res[0]==" ":
            new_string += res[1:]
            return new_string
        return res