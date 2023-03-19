import collections


class Solution(object):
    def totalFruit(self,fruits):
        count=collections.defaultdict(int)
        l,total,res=0,0,0
        for r in range(len(fruits)):
            count[fruits[r]]+=1
            total+=1

            while(len(count)>2):
                f=fruits[l]
                count[f]-=1
                total-=1
                l+=1
                if not count[f]:
                    count.pop(f)
            res=max(res,total)
        return res

    def TotalFruit(self, fruits):
        s=set()
        max=[]
        for item in fruits:
            count=0
            if item not in s:
                for i in range(len(fruits)):
                    if(item==fruits[i]):
                        count+=1
                s.add(item)
                max.append(count)
        max.sort()
        return max[len(max)-1]+max[len(max)-2],max
    
if __name__=="__main__":
    height = [3,3,3,1,2,1,1,2,3,3,4]
    e1=Solution()
    print(e1.totalFruit(height))
                    
                