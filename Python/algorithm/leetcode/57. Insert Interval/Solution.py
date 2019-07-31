class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals.pop(0)]
        
        while intervals:
            cur = intervals.pop(0)
            if ans[-1][-1] >= cur[1]:  pass
            elif ans[-1][-1] >= cur[0]:
                ans[-1] = [ans[-1][0], cur[1]]
            else: ans.append(cur)
        return ans