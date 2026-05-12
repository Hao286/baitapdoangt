class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # 2. Duyệt qua chuỗi một lần nữa để tìm ký tự đầu tiên có count == 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        
        # 3. Nếu không tìm thấy ký tự nào thỏa mãn
        return -1
        