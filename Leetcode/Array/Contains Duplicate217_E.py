class Solution(object):
    def containsDuplicate(self, nums):
        occurence={}
        for item in nums: 
            if item not in occurence:
                occurence[item]=1
            elif item in occurence:
                return True
        return False