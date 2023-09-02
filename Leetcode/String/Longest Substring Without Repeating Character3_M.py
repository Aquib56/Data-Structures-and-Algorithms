class Solution(object):
    set1=set()
    def LengthOfLongestSubstring(self, s):
        i=0
        j=1
        res=0
        if(len(s))==1:
            return 1
        if(len(s)==2):
            if(s[0]==s[1]):
                return 1
            else:
                return 2
        while(i<len(s)-1):
            count=0
            j=i+1
            self.set1.clear()
            while(j<len(s)-1 or s[j] not in self.set1):
                j+=1
                if(j>len(s)-1):
                    if(i==0):
                        self.set1.add(s[i])
                    break
                else:
                    count+=1
                    self.set1.add(s[j])                   
            i+=1
            res=max(res,len(self.set1))
        return res
    def lengthOfLongestSubstring(self, s):
        set1=set()
        l=0
        res=0
        for r in range(len(s)):
            print(set1)
            while s[r] in set1:
                set1.remove(s[l])
                l+=1
            set1.add(s[r])
            res=max(res,len(set1))
        return res
if __name__=="__main__":
    e1=Solution()
    print(e1.lengthOfLongestSubstring("abcabcbb"))
