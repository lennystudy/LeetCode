class Solution(object):
	#没想到回文数会用这一种方式
	#就是可以反方向还原出来的一定是回文数
	#如果不是回文数，肯定无法还原
	#
	#这里的定义是回文数因为有负号 所以肯定不是回文数了
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False
        ans = 0
        copy = x
        while copy:
        	ans = ans*10 + copy%10
        	copy = copy//10

        return x==ans



if __name__ == '__main__':
	print(Solution().isPalindrome(11131))