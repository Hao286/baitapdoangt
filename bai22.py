class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        count_map = {}
        ans = 0
        
        
        for a in nums1:
            for b in nums2:
                total = a + b
                count_map[total] = count_map.get(total, 0) + 1
        
       
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in count_map:
                    ans += count_map[target]
                    
        return ans