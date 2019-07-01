class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1: return False  
        
        stack = []        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0: return False

                peek = stack.pop()
                if (peek == "(" and s[i] == ")") or \
                    (peek == "{" and s[i] == "}") or\
                    (peek == "[" and s[i] == "]"):
                        pass
                else:
                    stack.append(peek)
                    stack.append(s[i])
        
        if len(stack) > 0: return False
        else : return True