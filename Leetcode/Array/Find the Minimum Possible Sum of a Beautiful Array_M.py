class Solution(object):
    def minimumPossibleSum(self, n, target):
        lenght=0
        res,i,map=[],1,{}
        while lenght<n:
            if i not in map:
                res.append(i)
                map[target-i]=1
                lenght+=1
            i+=1
        print(res)
        return sum(res)
s=Solution()
print(s.minimumPossibleSum(5,10))