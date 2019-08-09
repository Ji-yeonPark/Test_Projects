from collections import Counter


class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        words = {}
        for b in B:
            for k, v in Counter(b).items():
                if k not in words:
                    words[k] = v
                elif words[k] < v:
                    words[k] = v

        result = []
        for w in A:
            cnt = 0
            for k, i in words.items():
                if w.find(k) > -1 and w.count(k) >= i:
                    cnt += 1
            if cnt == len(words):
                result.append(w)
        return result
