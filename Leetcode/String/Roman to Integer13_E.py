class Solution(object):
    dict1={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    def romanToInt(self, s):
        count=0
        for i in range(len(s)):
            if i+1<len(s) and self.dict1[s[i]]<self.dict1[s[i+1]]:
                count-=self.dict1[s[i]]
            else:
                count+=self.dict1[s[i]]
        return count
if __name__=="__main__":
    arr="MCMXCIV"
    e1=Solution()
    print(e1.romanToInt(arr))       