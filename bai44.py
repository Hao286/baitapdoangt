class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        boxes = {}
        
        for ball in range(lowLimit, highLimit + 1):
            digit_sum = 0
            temp_ball = ball
            while temp_ball > 0:
                digit_sum += temp_ball % 10
                temp_ball //= 10
            
            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1
            
        return max(boxes.values())