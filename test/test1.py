i = 11000
str1 = str(i)
print(str1)
str2 = reversed(str1)
print(str1[::-1])

while False:
	print("value")

class Solution:
    # @return an integer
    def reverse(self, x):
        ans = 0
        if x >= 0:
            while x:
                ans = ans * 10 + x % 10
                x //= 10
                print(ans)
        else:
            return -self.reverse(-x)
        return ans
        
if __name__ == "__main__":
	p = Solution()
	print(p.reverse(123))
	print(type('he'))