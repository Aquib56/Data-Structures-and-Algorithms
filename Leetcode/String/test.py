class Solution(object):
    def longestCommonPrefix(self, strs):
        res=""
        i=0
        print(strs[0],strs[1])
        while i<=len(strs[0]) and i<=len(strs[1]):
            print(strs[0][i],strs[1][i],ResourceWarning)
            if strs[0][i]!=strs[1][i]:
                return res
            res+=strs[0][i]
            i+=1
        return res
s=Solution()
strs = ["flower","flow","flight"]
print(s.longestCommonPrefix(strs))