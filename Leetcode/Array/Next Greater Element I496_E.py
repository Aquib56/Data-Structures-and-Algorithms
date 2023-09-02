class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nums1Idx={n:i for i,n in enumerate(nums1)} 
        res=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr>stack[-1]:
                val=stack.pop()
                idx=nums1Idx[val]
                res[idx]=curr
            if curr in nums1Idx:
                stack.append(curr)
        return res
