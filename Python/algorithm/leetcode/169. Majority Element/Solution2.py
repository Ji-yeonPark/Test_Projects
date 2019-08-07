class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        tmp = defaultdict(lambda: 0)
        for n in nums:
            tmp[n] += 1
        return max(tmp, key=tmp.get)