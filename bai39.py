class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = zip(heights, names)
        people_sorted = sorted(people, key=lambda x: x[0], reverse=True)
        return [person[1] for person in people_sorted]