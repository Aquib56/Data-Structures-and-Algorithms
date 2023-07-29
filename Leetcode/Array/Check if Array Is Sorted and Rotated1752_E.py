class Solution(object):
    def check(self, nums):
        rotation_point = None
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rotation_point = i
                break

        if rotation_point is None:
            return True

        for i in range(rotation_point, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False

        if nums[0] < nums[-1]:
            return False

        return True
s1=Solution()
nums=[3,4,5,1,2]
print(s1.check(nums))