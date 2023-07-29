class Solution:
    def separateStones(self,K,arr):
        res=0
        whitebox=0
        blackbox=0
        for item in arr:
            if item==0:
                whitebox+=1
                if whitebox==K:
                    res+=1
                    whitebox=0
            if item==1:
                blackbox+=1
                if blackbox==K:
                    res+=1
                    blackbox=0
        if whitebox:
            res+=1
        if blackbox:
            res+=1
        return res
s=Solution()
arr= [1,0,1,1]
print(s.separateStones(3,arr))