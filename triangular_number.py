#truangular numbers are number which are the sum of the previous numbers

#this exercise prints the triangular number to the specified limit

number = input("enter a number: ")
num = -1
sum = 2
count = 1
output =""
while count <= int(number):
	num += sum
	for i in range(1, num+1):
		if num % i == 0:
			output += str(i) + ", "
	print( f"{num}: {output[0:-2]}")
	
	if num > 1:				
		sum += 1
	count += 1
	output = ""