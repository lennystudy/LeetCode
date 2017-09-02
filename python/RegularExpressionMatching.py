# 其实就是自己实现一遍正则
# 模拟正则表达式的. * 的用法
# 
# 比较符合自己正常的想法 使用递归
# 
# class Solution(object):
    # def isMatch(self, s, p):
    #     """
    #     :type s: str
    #     :type p: str
    #     :rtype: bool
    #     """
    #     # 考虑到如果正则为空的情况下
    #     if not p:
    #     	return not s
    #     # 递归到最后的情况
    #     if len(p) == 1:
    #     	if p[0] == "*":
    #     		return True
    #     	elif p[0] == ".":
    #     		if len(s) == 1:
    #     			return True
    #     		else:
    #     			return False
    #     	else:
    #     		if p[0] == s[0] and len(s) == 1:
    #     			return True
    #    	else:

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
        	return not s
        if len(p) == 1 or p[1] != '*':
        	if len(s) > 0 and (p[0] == s[0] or p[0] == '.'):
        		return self.isMatch(s[1:], p[1:])
        	elif p[0] == '*' and len(p) == 1:
        		return True
        	else:
        		return False
        else:
        	while len(s) > 0 and (p[0] == s[0] or p[0] == '.') :
        		if self.isMatch(s, p[1:]):
        			return True
        		s = s[1:]
        	return False

if __name__ == '__main__':
	solution = Solution()
	print(solution.isMatch('abad','abad*'))
	print(solution.isMatch("aab","c*a*b"))
         