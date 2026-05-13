class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = str(n)
        res = []
        for i in range(len(s)):
            if i > 0 and (len(s) - i) % 3 == 0:
                res.append('.')
            res.append(s[i])
        return "".join(res)