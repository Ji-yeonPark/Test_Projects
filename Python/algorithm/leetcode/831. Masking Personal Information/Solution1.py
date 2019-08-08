class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = S.lower()
        if S.find('@') > -1:
            name, addr = S.split('@')
            return "%s*****%s@%s".lower() % (name[0], name[-1], addr)
        else:
            import re
            S = re.sub('[-+( )]', '', S)
            phone = "***-***-%s" % (S[-4:])
            if len(S) > 10:
                return "+%s-%s" % ('*' * (len(S) - 10), phone)
            else:
                return phone