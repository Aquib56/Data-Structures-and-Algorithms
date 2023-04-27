class Solution(object):
    def isAnagram(self, s, t):
        letter={}
        if len(s)!=len(t):return False
        for item in s:
            if item in letter:
                letter[item]+=1
            else:
                letter[item]=1
        for item in t:
            if item in letter:
                letter[item]-=1
        for value in letter.values():
            if value!=0:
                return False
        return True
            

