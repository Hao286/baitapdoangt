class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 2. Duyệt qua từng ký tự trong chuỗi
        for i in range(n):
            # Lấy giá trị của ký tự hiện tại
            current_val = roman_map[s[i]]
            
            # Kiểm tra nếu ký tự hiện tại nhỏ hơn ký tự đứng sau nó
            if i + 1 < n and current_val < roman_map[s[i+1]]:
                # Nếu nhỏ hơn, ta trừ đi giá trị này (quy tắc IV, IX, XL...)
                total -= current_val
            else:
                # Nếu lớn hơn hoặc bằng, ta cộng vào tổng
                total += current_val
                
        return total
        