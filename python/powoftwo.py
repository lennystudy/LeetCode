#The method is not efficient
#I should try the bit method
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n%2==0:
        	n=n/2
        if n==1:
        	return True
        return False