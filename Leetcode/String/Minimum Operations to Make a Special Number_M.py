class Solution(object):
    def minimumOperations(self, num):
        s=str(num)
        if int(s)%25==0:
            return 0
        op=0
        i=len(s)-1
        while s:
            print(i,s)
            if int(s[len(s)-2]+s[len(s)-1])%25==0 or (s[len(s)-1]=="0" and s[len(s)-2]=="0"):
                return op
            elif s[i]=="0":
                i-=1
            else:
                s=s[0:i]+s[i+1:len(s)]
                op+=1
                i=len(s)-1
        return op
    
s=Solution()
num = "2713539"
print(s.minimumOperations(num))