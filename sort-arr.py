def lensort(arr:list):
	for i in range(len(arr)):
		for j in range(0, len(arr)-1):
			if len(arr[j]) > len(arr[j+1]):
				z = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = z
	print(arr)		
lensort(["sense", "jaye", "name","gshdbxjs",  "typ", "joshua", "a", "bc"])

#def lensowt(a):
#	ame',  'she',  'hi',  'n']
#	if len(a) == 1:
#		return 1
#	else:
#		return lensowt(a) - lensowt(a + 1)
#	
#lensowt(a)