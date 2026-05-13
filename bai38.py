from collections import Counter

class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counts = Counter(s)
        return len(set(counts.values())) == 1