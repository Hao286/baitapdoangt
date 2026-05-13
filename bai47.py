class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        
        sorted_digits = sorted(list(digits), reverse=True)
        
        if len(sorted_digits) >= 2:
            return sorted_digits[1]
        
        return -1