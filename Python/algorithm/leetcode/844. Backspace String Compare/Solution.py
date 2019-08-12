class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        w1 = self.check(list(S))
        w2 = self.check(list(T))

        if w1 == w2: return True
        else: return False        
        
    def check(self, word):
        _word = []
        
        for i in word:
            if i == "#":
                if _word:  _word.pop()
            else:
                _word.append(i)
        return _word