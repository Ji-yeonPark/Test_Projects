class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        tmp = defaultdict(lambda:0)
        
        for n in nums:
            tmp[n] += 1
        return [key for key, val in tmp.items() if val > len(nums) / 3]