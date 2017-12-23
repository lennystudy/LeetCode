# 这个就是目前的手机里面按数字键出字母匹配的功能
# 只是当前手机的话，会做一个过滤，把不可能的组合给去掉
# 其实难点是在于数据结构的选择 如何选择合适的数据结构来进行存储
# 
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
        	return []
        key_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result = [""]
        for digit in digits:
        	choices = key_map[digit]
        	m,n = len(choices),len(result)
        	result.extend([result[i%n] for i in range(n, n*m)])
        	for i in range(m*n):
        		result[i] = result[i] + choices[i//n]
        return result 	

# 还有另外一种更优美的方式，采用递归的方式

    def letterCombinations1(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
        	return []
        dictionary = ["","","abc","def","ghi","jkl","mno","pars","tuv","wxyz"]
        result = []
        self.solve(digits, dictionary, 0 , "", result)
        return result

    def solve(self, digits, dictionary, length, cur ,result):
    	if length == len(digits):
    		result.append(cur)
    	else:
    		for data in dictionary[int(digits[length])]:
    			self.solve(digits, dictionary, length + 1, cur+data, result)


if __name__ == '__main__':
	digits = "2356"
	print(Solution().letterCombinations1(digits))
	print(len(Solution().letterCombinations(digits)))    