class Solution(object):
    def addBinary(self, a, b):
        carry=0
        updated=""
        a,b=a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            digitA=ord(a[i])-ord("0") if i < len(a) else 0
            digitB=ord(b[i])-ord("0") if i < len(b) else 0
            total=digitA+digitB+carry
            char=str(total%2)
            updated=char+updated
            carry=total//2
        if carry:
            updated="1"+updated
        return updated
e1=Solution()
print(e1.addBinary("11","1"))
