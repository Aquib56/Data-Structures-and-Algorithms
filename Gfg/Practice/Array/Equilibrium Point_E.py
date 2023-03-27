def equilibriumPoint_Naive(A, N):
    element_idx=1
    while element_idx<len(A)-1:
        left_sum,right_sum=0,0
        left,right=element_idx-1,element_idx+1
        while left>=0:
            left_sum+=A[left]
            left-=1
        while right<=len(A)-1:
            right_sum+=A[right]
            right+=1
        if left_sum==right_sum:
            return element_idx+1
        element_idx+=1
    return -1
def equilibriumPoint(A,N):
    if len(A)==1:
        return 1
    total_sum,curr_sum,idx=0,0,0
    for item in A:
        total_sum+=item
    while idx<=len(A)-1:
        curr_sum+=A[idx]
        idx+=1
        if curr_sum==total_sum-(curr_sum+A[idx]):
            return idx+1
    return -1
    
arr=[1,3,5,2,2]
print(equilibriumPoint(arr,5))
