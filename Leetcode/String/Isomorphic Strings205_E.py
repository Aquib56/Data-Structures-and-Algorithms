class Solution(object):
    def isIsomorphic(self, s, t):
        i=0
        map={}
        while i<len(s):
            print(map)
            if s[i] not in map and t[i] in map.values():
                print(1)
                return False
            if s[i] not in map:
                map[s[i]]=t[i]
            elif map[s[i]]!=t[i]:
                print(2)
                return False
            i+=1
        return True
s1=Solution()
s = "egg"
t = "add"
print(s1.isIsomorphic(s,t))
