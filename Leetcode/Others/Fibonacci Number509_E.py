class Solution(object):
    def fib(self, n):
        if n==2:
            return 2
        def helper(n):
            if n==1:
                return 1
            elif n==0:
                return 0
            elif n<0:
                return
            return helper(n-1)+helper(n-2)
        return helper(n)
         

s=Solution()
print(s.fib(2))

    