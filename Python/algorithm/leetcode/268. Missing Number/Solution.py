class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) != nums[-1]: 
            return len(nums)
        
        for i, x in enumerate(nums):
            if i != x: return i