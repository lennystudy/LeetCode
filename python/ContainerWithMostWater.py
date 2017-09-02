# 不以英语为母语，阅读起来确实还是比较吃亏
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, max_area = 0,len(height)-1, 0
        while i < j:
        	max_area = max(max_area, min(height[j],height[i])*(j-i))
        	if height[i] < height[j]:
        		i = i + 1
        	else:
        		j = j - 1
        return max_area

if __name__ == '__main__':
	print(Solution().maxArea([1,2,3,4,5,6]))