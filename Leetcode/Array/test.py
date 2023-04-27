nums=[1,2,4,5]

def bruh(nums,count):
    if not nums:
        print(count)
        return
    count+=nums[0]
    bruh(nums[1:],count)
bruh(nums,0)