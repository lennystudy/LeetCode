class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums,i= sorted(nums),0
        res = []
        while i < len(nums)-2:
        	j = i+1
        	k = len(nums)-1
        	while j < k:
        		if nums[i]+nums[j]+nums[k] > 0:
        			k = k-1
        		elif nums[i]+nums[j]+nums[k] < 0:
        			j = j+1
        		else:
        			res.append([nums[i],nums[j],nums[k]])
        			j,k = j+1,k-1
        			while j < k and nums[j] == nums[j-1]:
        				j = j+1
        			while j < k and nums[k] == nums[k+1]:
        				k = k-1
        	i = i+1
        	while i < len(nums)-2 and nums[i] == nums[i-1]:
        		i += 1
        return res




if __name__ == '__main__':
	nums = [-2,0,1,1,2]
	print(Solution().threeSum(nums))