class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = int(a,2) + int(b,2)
        ans = str(bin(ans))
        return ans[2:]

if __name__ == '__main__':
	p = Solution()
	a = "1101"
	b = "1001"
	print(p.addBinary(a,b))