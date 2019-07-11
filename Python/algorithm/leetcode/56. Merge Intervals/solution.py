class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if len(intervals) == 0: return intervals
        
        intervals.sort()
        list = [intervals.pop(0)]
        
        while intervals:    
            cur = intervals.pop(0)
            if list[-1][-1] >= cur[1]:
                pass
            elif list[-1][-1] >= cur[0]:
                list[-1] = [list[-1][0], cur[-1]]
            else:
                list.append(cur)
        
        return list