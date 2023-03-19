class Solution(object):
    def intToRoman(self, num):
        list=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],
              ["L",50],["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        res=""
        for sym ,val in reversed(list):
            if num//val:
                count=num//val
                res+=(count*sym)
                num=num%val
        return res
x=Solution()
print(x.intToRoman(1993))