class Solution(object):
    def shuffle(self, nums, n):
        k=0
        abc=[None]*(2*n)
        for i in range(n):
            abc[k]=nums[i]
            k+=1
            abc[k]=nums[i+n]
            k+=1
        return abc
if __name__=="__main__":
    arr=[1,3,5,6,8,7]
    e1=Solution()
    print(e1.shuffle(arr,3))
