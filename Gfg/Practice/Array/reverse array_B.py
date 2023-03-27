def reverse(nums):
    res=[]
    for i in range(len(nums)-1,-1,-1):
        res.append(nums[i])
    return res
arr=[3,1,54,6,2]
print(reverse(arr))