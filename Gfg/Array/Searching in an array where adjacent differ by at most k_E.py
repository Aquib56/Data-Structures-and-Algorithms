def search (arr, n, x, k) : 
    i=0
    while i<n:
        if arr[i]==x:
            return i
        i+=max(1,abs(arr[i]-x)//k)
    return -1
nums=[20, 40, 50, 70, 70, 60]
print(search(nums,len(nums),100,20))