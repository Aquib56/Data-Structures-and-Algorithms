class Solution:
    def operation(self,a,b,o):
        print(a,b,o)
        a=int(a)
        b=int(b)
        if o=="+":
            return a+b
        elif o=="-":
            return a-b
        elif o=="*":
            return a*b
        elif o=="/":
            return a/b
    def evaluatePostfix(self, S):
        operators=["+","-","*","/"]
        res=0
        print(S)
        while len(S)>2:
            i=0
            while i<=len(S)-1 and S[i] not in operators:
                i+=1
            temp=self.operation(S[i-1],S[i-2],S[i])
            S=S[:i-2] +str(temp) +S[i+1:]
            print(S,temp)
        return temp
s1=Solution()
print(s1.evaluatePostfix("342+*5*"))