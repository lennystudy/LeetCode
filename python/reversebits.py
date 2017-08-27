class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
        	ans = ans<<1
        	ans = ans|(n&1)
        	n = n>>1
        return ans


if __name__ == '__main__':
	print(Solution().reverseBits(11111111111111111111111111111111111111111111111))