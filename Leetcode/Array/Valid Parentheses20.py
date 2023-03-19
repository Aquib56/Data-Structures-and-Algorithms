class Solution(object):
    def isValid(self, s):
        stack=[]
        mapping={")":"(","}":"{","]":"["}
        for item in s:
            if item in mapping:
                if stack and stack[-1]==mapping[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return True if not stack else False
if __name__=="__main__":
    arr="(]"
    e1=Solution()
    print(e1.isValid(arr))                
