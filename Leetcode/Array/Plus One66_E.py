class Solution(object):
    def plusOne(self, digits):
        carry,i=1,len(digits)-1
        while carry:
            if i>=0:
                if digits[i]==9:
                    digits[i]=0
                else:
                    digits[i]+=1
                    carry=0
            else:
                digits=[1]+digits
                carry=0
            i-=1
        return digits

                
if __name__=="__main__":
    nums=[1,8,9]
    e1=Solution()
    print(e1.plusOne(nums))

                
