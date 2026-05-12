class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Lấy chuỗi đầu tiên làm mốc để so sánh
        base = strs[0]
        
        for i in range(len(base)):
            # Duyệt qua các chuỗi còn lại trong danh sách
            for s in strs[1:]:
                # Nếu chỉ số i vượt quá độ dài chuỗi s 
                # hoặc ký tự tại vị trí i không khớp
                if i == len(s) or s[i] != base[i]:
                    return base[:i]
        
        return base
        """
        :type strs: List[str]
        :rtype: str
        """
        