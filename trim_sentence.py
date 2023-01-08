#remove the excess underscore from the inputed string and return a string with only one underscore 

def trim_sent(sentence):

	new_sentence = ""
	my_sent= [i for i in sentence]
	
	for i in range(len(my_sent)):
		
		if my_sent[i].isalpha():
			new_sentence += my_sent[i]
			
		elif my_sent[i +1].isalpha():
			new_sentence += my_sent[i]
	
	print(new_sentence)

trim_sent("my_____name___is___joshua")