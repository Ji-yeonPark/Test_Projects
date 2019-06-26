class Solution:
    def threeSum(self, nums):
        arr = []

        for i in range(len(nums) - 2):
            j = i + 1

            while j < len(nums) -1:
                x = nums[i]
                y = nums[j]
                sums = x + y
                _sorted = sorted([x,y])
                if (0 - sums) in nums[j+1:]:
                    _arr = sorted([x, y, 0 - sums])
                    if _arr not in arr:
                        arr.append(_arr)
                j += 1
        return arr