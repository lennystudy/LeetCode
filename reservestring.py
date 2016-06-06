class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        return s

if __name__ == '__main__':
	p = Solution()
	print(p.reverseString('hello'))