class Solution(object):
    def merge(self, nums1, m, nums2, n):
            j,i,inc=0,m-1,0
            if not nums1:
                for item in nums2:
                    nums1.append(item)
            elif not nums2:
                nums1=nums1
            else:
                while j<len(nums2):
                    while i>=0 and nums2[j]<nums1[i]:
                        nums1[i+1]=nums1[i]
                        i-=1
                    nums1[i+1]=nums2[j]
                    inc+=1
                    j+=1
                    i=(m-1)+inc
    def betterKinda(self, nums1, m, nums2, n):
        last=m+n-1
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[last]=nums1[m-1]
                m-=1
            else:
                nums1[last]=nums2[n-1]
                n-=1
            last-=1
        while n>0:
            nums1[last]=nums2[n-1]
            n-=1
            last-=1
            
s=Solution()
nums1 = [1,5,7,0,0,0]
nums2 = [2,3,9]
print(nums1,nums2)
s.betterKinda(nums1,3,nums2,3)
print(nums1)
