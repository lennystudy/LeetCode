class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=0
        while n!=0:
            n=n&(n-1)
            num=num+1
        return num

test=Solution()
print(test.hammingWeight(12))