class Solution(object):
    def average(self, salary):
        salary.sort()
        sum=0
        for i in range(1,len(salary)-1):
            sum+=salary[i]
        sum=round(float(sum)/(len(salary)-2),4)
        return sum
s1=Solution()
nums=[48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
print(s1.average(nums))