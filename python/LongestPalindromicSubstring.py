# 
# 最长回文字符串
# 
# 全部遍历是肯定可以解决的最笨的办法
# 
# 如何彻底解决所有回文相关的问题呢
# 
# 问题应该在于如何最少遍历已有的字符串。
# 
# 回文字符串至少以中间某一个字符为中心，也就是说我们遍历的时候，可以以中心字符向左右扩展
# 
# 避免重复的话应该是
# 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = self.preProcess(s)
        palindrome = [0] * len(string)
        center, right = 0, 0
        for i in range(1, len(string)-1):
        	i_mirror = 2*center - i
        	if right > i:
        		palindrome[i] = min(right -i , 	palindrome[i_mirror])
        	else:
        		palindrome[i] = 0
        	while string[palindrome[i] + i + 1] == string[i - 1 - palindrome[i]]:
        		palindrome[i] += 1
        # 还需要及时更新center 和 right的值
        	if i + palindrome[i] > right:
        		center, right = i, palindrome[i] + i

        # 找到了最长的字符串所在的位置之后就可以为所欲为了
        max_len, max_center = 0, 0
        for x in range(1, len(string)-1):
        	if palindrome[x] > max_len:
        		max_center = x
        		max_len = palindrome[x]
        start = (max_center - 1 - max_len) // 2

        return s[start: (start + max_len)]

    def preProcess(self, s):
    	if not s:
    		return "^$"
    	s1 = "^"
    	for x in s:
    		s1 += "#" + x
    	return s1 + "#$"

if __name__ == '__main__':
	Solution = Solution()
	s = "aaaaa"
	print(Solution.longestPalindrome(s))