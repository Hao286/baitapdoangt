class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        smaller_counts = {}
        
        for i, num in enumerate(sorted_nums):
            if num not in smaller_counts:
                smaller_counts[num] = i
        
        return [smaller_counts[num] for num in nums]
        