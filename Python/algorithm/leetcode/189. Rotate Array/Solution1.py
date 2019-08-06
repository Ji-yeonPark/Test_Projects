class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            n = nums.pop()
            nums.insert(0, n)
            k -= 1
