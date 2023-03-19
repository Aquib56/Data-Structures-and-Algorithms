class Solution(object):
    def isPalindrome(self, s):
        alpha=""
        for item in s:
            if item.isnumeric():
                alpha+=item
            elif item.isalpha():
                alpha+=item
        alpha=alpha.lower()
        print(alpha)
        # if alpha==alpha[::-1]:
        #     return True
        # else:
        #     return False
        f,r=0,len(alpha)-1
        while f<r and alpha[f]==alpha[r]:
            f+=1
            r-=1
        if f>=r:
            return True
        else:
            return False
    def ispalindrome(self,s):
s1=Solution()
s="A man, a plan, a canal: Panam"
print(s1.isPalindrome("0P"))

