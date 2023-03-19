class Solution(object):
    def IsValid(self, s):
        bollean=True
        mapping={"{":"}","(":")","[":"]"}
        i=0
        j=0
        while(i<len(s)):
            if(s[i]=="{" or s[i]=="[" or s[i]=="("):
                while(j<len(s)-1 and s[j]!=mapping[s[i]]):
                    j+=1
                print(f"{s[i]},{i},{j}")
                if(j>len(s)-1):
                    return False
                else:
                    bollean=True
                j+=1
            i+=1
        return bollean
    def isValid(self,s):
        stack=[]
        closeToopen={")":"(","]":"[","}":"{"}
        for item in s:
            if item in closeToopen:
                if stack and stack[-1]==closeToopen[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return True if not stack else False

        
 
if __name__=="__main__":
    arr="()"
    e1=Solution()
    print(e1.isValid(arr))                
