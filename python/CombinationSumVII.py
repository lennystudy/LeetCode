# 跟之前题目的不同点在于是否要去重
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combination(sorted(candidates),target, [], result, 0)
        return result

    def combination(self, candidates, target, temp, result, start):
    	if target == 0:
    		result.append(list(temp))
    	prev = 0
    	while start < len(candidates) and target >= candidates[start]:
    		if prev != candidates[start]:
    			temp.append(candidates[start])
    			self.combination(candidates, target-candidates[start], temp, result, start+1)
    			temp.pop()
    			prev = candidates[start]
    		start = start + 1

if __name__ == '__main__':
	candidates = [2,2,2,2,3,4,5,6]
	target = 7
	print(Solution().combinationSum2(candidates, target))