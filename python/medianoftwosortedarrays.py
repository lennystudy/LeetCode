class Solution(object):
    #我没有理解错的话，应该是归并排序
    #然后在排序的基础上进行筛选
    #如果长度为奇数，则是中间的那个数
    #如果长度为偶数，则应该取两个数组的中间的那两个数的平均数
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = self.mergesort(nums1, nums2)
        length = len(array)
        if length %  2 == 1:
        	return array[length//2]
        else:
        	return (array[length//2] + array[length//2 - 1])/2
            # python版的归并排序
    def mergesort(self, array1, array2):
        if array1 == "" or array2 == "":
            return array1 + array2
        i,j = 0,0
        ans = []
        while  i != len(array1) or j != len(array2):
            if i == len(array1):
                ans += array2[j:]
                break
            if j == len(array2):
                ans += array1[i:]
                break
            if array1[i] < array2[j]:
                ans.append(array1[i])
                i += 1
            else:
                ans.append(array2[j])
                j += 1
        return ans


        

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    p = Solution()
    print(p.findMedianSortedArrays(nums1,nums2))
