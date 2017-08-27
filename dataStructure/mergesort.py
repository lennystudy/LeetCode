# python版的归并排序
def mergesort(array1, array2):
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
	array1 = [7,89,105]
	array2 = [8,10,11]
	print(mergesort(array1, array2))

