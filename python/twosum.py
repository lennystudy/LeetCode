class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
        	return None
        sortNums = nums
        answer = [0,0]
        for x in range(0,len(nums)-1):
        	targetNum = target - nums[x]
        	if targetNum in nums[x+1:len(nums)]:
        		answer[0] = x
        		answer[1] = nums[x+1:len(nums)].index(targetNum) + x + 1
        		print(x)
        		break
        return answer


if __name__ == '__main__':
	p = Solution()
	nums = [0,4,3,0]
	target = 0
	print(p.twoSum(nums,target))