# 主要是自己本身也不了解罗马字
# 不过思想本身是互通的
# 就是任意进制的转换
# 都是从大到小去转换
# 
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        numeral_map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        result, numeral_keys = "", sorted(numeral_map.keys())
        while num > 0:
        	for key in reversed(numeral_keys):
        		while num//key > 0:
        			num = num - key
        			result += numeral_map[key]  			
       	return result


if __name__ == '__main__':
	num = 366
	print(Solution().intToRoman(num))
	print(num)