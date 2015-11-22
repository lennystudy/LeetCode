#find the nth uglynumber
#This method is not efficiency
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer=1
        count=1
        while n!=0:
        	while answer%2==0:
        		answer=answer/2
        	while answer%3==0:
        		answer=answer/3
        	while answer%5==0:
        		answer=answer/5
        	if answer==1:
        		n=n-1
        	if n==0:
        		break
        	count=count+1
        	answer=count
        return count
        	

test=Solution()
print(test.nthUglyNumber(279))