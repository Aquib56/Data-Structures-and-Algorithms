class Solution(object):
    def largestOddNumber(self, num):
        max=-1
        for i in range(len(num)-1,-1,-1):
            print(i)
            curr=int(num[i])
            if curr%2!=0 and curr>=max:
                return num[0:i+1]
        return " "




s=Solution()
print(s.largestOddNumber("52"))