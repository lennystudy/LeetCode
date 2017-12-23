# Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
        	return ""
        result = strs[0]
        for string in strs[1:]:
        	i = 0
        	while i < len(string) and i < len(result) and string[i] == result[i]:
        		i = i + 1
        	result = result[:i]
        return result
        	

if __name__ == '__main__':
	arr1 = ["abc","ab","ab"]
	print(Solution().longestCommonPrefix(arr1))
        