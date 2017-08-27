class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
        	return None
        dict = {}
        ans = []
        nums.sort()
		for x in nums:
			if x in dict.keys():
				dict[x] = dict[x] + 1
			else:
				dict[x] = 1





if __name__ == '__main__':
	p = Solution()
	array = [1,2,3,4,1,1]
	print(p.majorityElement(array))