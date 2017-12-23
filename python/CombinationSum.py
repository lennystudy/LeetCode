# 也算是动态规划的一种吧
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.combination(sorted(candidates), target, [], 0, result)
        return result
    # 如果最后target不等于0 但是不满足下面的条件，其实也没有再计算的可能了
    def combination(self, candidates, target, temp, count, result):
    	if target == 0:
    		result.append(list(temp))
    	while count < len(candidates) and target - candidates[count] >= 0:
    		temp.append(candidates[count])
    		self.combination(candidates, target-candidates[count], temp, count, result)
    		temp.pop()
    		count = count +1


if __name__ == '__main__':
	candidates = [2,3,5,7]
	target = 7
	print(Solution().combinationSum(candidates, target))
