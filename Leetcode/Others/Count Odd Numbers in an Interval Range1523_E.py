class Solution(object):
    def countOdds(self, low, high):
        lenght=high-low+1
        count=lenght//2
        if lenght%2 and low%2:
            count+=1
        return count
if __name__=="__main__":
    e1=Solution()
    print(e1.countOdds(12,13))
