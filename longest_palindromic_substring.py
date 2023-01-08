#find the longest palindromic contiguous substring if there are more than one return any 

#asked by Amazon


#palinfrom a function to check if a word and it reverse are the same

def palindrom(insert):
	if len(insert) == 0 or len(insert) == 1:
		return True
		
	elif insert[0]  == insert[-1]:
		return palindrom(insert[1:-1])
			
	return False
	

def pal(word:str) -> str:
	substrings =[]
	for i in range(0, len(word)-1):
		for j in range(len(word)-1, 0, -1):
			if word[i] == word[j]:
				#using tge above function to check if the string is palindrom
				pal = palindrom(word[i:j+1])
				if pal == True:
					arr.append(word[i:j+1])
					
#checking for the substring with the highest length		
	max = arr[0]
	for i in range(len(arr)):
		if len(arr[i]) > len(max):
			max = arr[i]
	print(max)
	
	
pal("bananabbgghggbbjkgfg")

