class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        if x >= 0:
        	while x:
        		ans = ans*10 + x%10
        		x = x//10
        	return ans if ans <= 2147483647 else 0
        else:
        	return -self.reverse(-x)


if __name__ == '__main__':
	print(Solution().reverse(-1534236469))