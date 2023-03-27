class Solution:
    def ispar(self,x):
        if len(x)==1:
            return False
        stack=[]
        closedpar={"}":"{","]":"[",")":"("}
        for item in x:
            if item =="(" or item =="[" or item =="{" :
                stack.append(item)
            elif item in closedpar:
                if not stack:
                    return False
                if closedpar[item]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
e1=Solution()
print(e1.ispar("((}"))


