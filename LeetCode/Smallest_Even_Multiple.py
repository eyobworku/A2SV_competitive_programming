class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2 == 0:
            return n
        return 2*n
        """
        :type n: int
        :rtype: int
        """
        