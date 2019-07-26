class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 0: return 1
        elif nums[-1] < 0: return 1
        
        i = 1
        while True:
            if i not in nums: return i
            i += 1