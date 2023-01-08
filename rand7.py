#using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,  implement a function rand7()  that returns an integer from 1 to 7 (inclusive)

#asked by Two sigma


import random


def rand5() -> int:
	return random.randint(1, 5)
	
def rand7() -> int:
	num = rand5()
	num7 = random.randint(1, num+2)
	return num7
print(rand7())