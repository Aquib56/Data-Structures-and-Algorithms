class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        i=len(s)-1
        while(i>-1):
            if(s[i]==" "):
                i-=1
            else:
                print(i)
                while(s[i]!=" "):
                    count+=1
                    i-=1
                    if i==-1:
                        return count
                return count


if __name__=="__main__":
    e1=Solution()
    print(e1.lengthOfLastWord("a"))