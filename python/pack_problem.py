# 背包问题详解
class Solution(object):
	# 0 1背包问题
	def pack_solution(self, weights, values, max_weight):
		if len(weights) != len(values):
			return False
		# 也要先定义收敛条件
		length = len(weights)
		result = [[0 for x in range(0,max_weight+1)] for y in range(0,length)]
		for i in range(1,length):
			for j in range(1,max_weight+1):
				result[i][j] = result[i-1][j]
				if j > weights[i-1] and result[i-1][j] < result[i-1][j-weights[i-1]] + values[i-1]:
					result[i][j] = result[i-1][j-weights[i-1]] + values[i-1]
		print(result)
		print(max_weight)
		return result[length-1][max_weight]


	def pack_solution1(self,p,n):
		result = [0 for k in range(0, n+1)]
		print(result)
		for j in range(1,n+1):
			q = -100
			for i in range(1,j+1):
				q = max(q, p[i]+result[j-i])
			result[j] = q
		print(result)
		return result[n]



if __name__ == '__main__':
	weights = [0,2,2,3,4,5]
	values = [0,5,3,4,5,6]
	max_weight = 10
	print(Solution().pack_solution(weights, values, max_weight))

	# weights = range(0,11)
	weights = [0,1,2,3,4,5,6,7,8,9,10]
	values = [0,1,5,8,9,10,17,17,20,24,30]
	max_weight = 7
	print(Solution().pack_solution(weights, values, max_weight))

	p = [1,3,4,5,7]
	n = 3
	print(Solution().pack_solution1(p,n))