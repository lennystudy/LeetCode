# 我终于明白这道题为什么不一样了，比如要求7 从头到尾遍历的话，肯定把1,2,3放进去了，然后发现求不出结果。。
# 应该怎么遍历呢，首尾遍历，还是先放进去，发现不合适再吐出来
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        combination = [1,2,3,4,5,6,7,8,9]
        self.combination(combination, k, n, [], 0, result)
        return result

    def combination(self, combination,k, n, temp, start, result):
    	print(n)
    	if n == 0:
    		print(n)
    		result.append(list(temp))
    	while start < k and n >= combination[start]:
    		temp.append(combination[start])
    		self.combination(combination,k-1, n - combination[start], temp, start + 1, result)
    		combination.pop()
    		start = start + 1

if __name__ == '__main__':
	k = 3
	n = 7
	print(Solution().combinationSum3(k,n))