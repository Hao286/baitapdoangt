class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Duyệt từ phải sang trái (từ hàng đơn vị lên)
        for i in range(n - 1, -1, -1):
            # Nếu chữ số hiện tại < 9, chỉ cần cộng 1 và trả về mảng ngay
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # Nếu chữ số là 9, nó sẽ trở thành 0 và tiếp tục vòng lặp để nhớ sang trái
            digits[i] = 0
            
        # Nếu thoát khỏi vòng lặp mà chưa return, nghĩa là tất cả các số đều là 9
        # (Ví dụ: [9, 9] -> biến thành [0, 0]). Ta cần thêm 1 vào đầu mảng.
        return [1] + digits
        