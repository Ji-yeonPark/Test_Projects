class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        import collections
        dic = collections.Counter(words)
        tmp = []
        for key, val in dic.items():
            tmp.append([key, val])            
        tmp.sort(key = lambda x: (-x[1], x[0]))
        
        return [tmp[i][0] for i in range(k)]