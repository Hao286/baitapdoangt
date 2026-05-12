class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        
        total_time = 0
        
        for i in range(len(timeSeries) - 1):
            actual_duration = min(timeSeries[i+1] - timeSeries[i], duration)
            total_time += actual_duration
            
        return total_time + duration