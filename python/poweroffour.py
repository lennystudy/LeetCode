class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        while num%4 == 0 and num >= 4:
            num = num//4
        if num == 0 or num == 1:
            return True
        return False

        
if __name__ == '__main__':
	print(Solution().isPowerOfFour(23))
	print(Solution().isPowerOfFour(0))
	print(Solution().isPowerOfFour(-23))
	print(Solution().isPowerOfFour(16))
	print(Solution().isPowerOfFour(8))