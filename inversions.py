#we can determine how out of order an array A is by counting the number of inversions it has. Two element A[i] and A[j] form an inversion if A[i] > A[j] but i < j .That is ,  a smaller element appears before a larger one.

#given an array,  count the number of inversion it has

#an empty or sorted array has zero inversion. The array [2, 4, 1, 3, 5] has three inversion (2, 1), (4, 1), (4, 3).

#asked by google


def count_inversion(arr) -> int:
	count = 0
	for i in range(len(arr) - 1, 0, -1):
		for j in range(i):
			if arr[j] > arr[j+1]:
				count += 1
	return count
	
arr1 = [2, 4, 1, 3, 5]	
print(count_inversion(arr1))