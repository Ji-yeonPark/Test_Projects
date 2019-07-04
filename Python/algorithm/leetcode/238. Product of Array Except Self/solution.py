class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L, R = [0] * len(nums), [0] * len(nums)
        L[0], R[-1] = 1, 1
        
        for i in range(len(nums)-1):
            L[i+1] = nums[i] * L[i]
        for i in range(len(nums)-1, 0, -1):
            R[i-1] = nums[i] * R[i]
            L[i-1] = R[i-1] * L[i-1]
            
        return L