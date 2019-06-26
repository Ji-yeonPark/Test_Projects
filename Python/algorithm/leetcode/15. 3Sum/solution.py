class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr = []
        nums = sorted(nums)
        l = len(nums)

        for i in range(l - 2):
            if (nums[i] != nums[i-1]) or i == 0:
                j, k = i + 1, l - 1
                target = -nums[i]

                while j < k:
                    sums = nums[j] + nums[k]
                    if sums < target:
                        j += 1
                    elif sums > target:
                        k -= 1
                    else:
                        arr.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while k > j and nums[k] == nums[k-1]:
                            k -= 1
                        j += 1
                        k -= 1

        return arr
