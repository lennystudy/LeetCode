

#算法分析
#从头到尾遍历，取一个变量保存最长的字符串
#从头开始，获得每一个字母开始的子字符串
#进行比较，若更长则替换前面的变量
#
#
#其实更好的方法是维护一张表，记录其中每一次的遍历 还有把上次的遍历给清除掉
#如果在这个点遇到了重复的 那么当前点到重复点之间，不可能有比当前长度更长的子字符串了吧
#
#貌似我存最长的字符串还没有存这对应的时间更方便
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        length = 0
        visited = [False for _ in range(256)]
        for i,char in enumerate(s):
        	if visited[ord(char)]:
        		while s[start] != char:
        			visited[ord(s[start])] = False
        			start = start + 1
        		start = start + 1
        	else:
        		visited[ord(char)] = True
        	length = max(length,i-start+1)
        return length
        	


    def test(self):
    	return 0

if __name__ == '__main__':
	p = Solution()
	str = "hello"
	print(p.lengthOfLongestSubstring(str))
	
