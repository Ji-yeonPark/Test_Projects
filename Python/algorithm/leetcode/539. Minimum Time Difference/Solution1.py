class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        tTable = []
        for time in timePoints:
            tTable.append(self.converter(time))
            if time.startswith('0'):
                time = "{}:{}".format(str(int(time.split(":")[0]) + 24), time.split(":")[-1])
                tTable.append(self.converter(time))
                
        min = 60 * 24
        while len(tTable) > 1:
            a = tTable.pop(tTable.index(max(tTable)))
            b = tTable.pop(tTable.index(max(tTable)))
                           
            if min > a - b: min = a - b
            if min == 0: return min
            
            tTable.append(b)
        return min
        
    def converter(self, time):
        H, M = time.split(":")
        return (int(H) * 60) + int(M)