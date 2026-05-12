class Solution(object):
    def isAnagram(self, s, t):
        # Nếu độ dài khác nhau, chắc chắn không phải anagram
        if len(s) != len(t):
            return False
        
        # Sắp xếp cả hai chuỗi và so sánh
        return sorted(s) == sorted(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        