#The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

#For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

#You may also use a list or array to represent a set.

#asked by google

def gen_pow_set(super_set) -> list:
	output = set()
	output.add(())
	for i in range(len(super_set)):
		output.add((super_set[i], ))
		for j in range(i+1, len(super_set)):
			output.add((super_set[i], super_set[j]))
		# as the length of the setObj increase, continue the pattern of the loops
	output.add(tuple(super_set))
	print(len(output))
	return sorted(output, key=len)
	
print(gen_pow_set([1, 2, 3]))