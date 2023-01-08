#fizzbuzz using decorators


def fizzbuzz(func):
	""" return fizz if number is a multiple of 3, buzz if 5, and fizzbuzz if 15
	"""
	value = func(0)
	
	def main_func(value):
		if value % 5 == 0 and value % 3 == 0:
			return "fizzbuzz"
		elif value % 5 == 0:
			return "fizz"
		elif value % 3 == 0:
			return "buzz"
	return main_func
	
@fizzbuzz
def number(num):
	return num
	
if __name__ == "__main__":
	output = number(45)
	print(output)