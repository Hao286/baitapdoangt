class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        
        for i in range(1, len(res), 2):
            char = res[i-1]
            shift_val = int(res[i])
            res[i] = chr(ord(char) + shift_val)
            
        return "".join(res)