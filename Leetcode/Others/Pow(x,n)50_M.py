class Solution(object):
    def myPow(self, x, n):
        if x==0:
            return 0
        def helper(x,n):
            if n==0:
                return 1
            res=helper(x,n//2)
            res=res*res
            if n%2==0:
                return res
            else:
                return res*x
        res=helper(x,abs(n))
        return res if n>=0 else 1/res
s=Solution()
print(s.myPow(2,10))