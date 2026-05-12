class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        max_allowed = len(candyType) // 2
        
        # 2. Tìm số lượng loại kẹo thực tế (các giá trị duy nhất)
        unique_types = len(set(candyType))
        
        # 3. Kết quả là số nhỏ hơn giữa hai giá trị trên
        return min(unique_types, max_allowed)