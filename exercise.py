# Example 1
def name_shuffle(txt):
	list_txt = list(txt)
	first = ''.join(list_txt[(list_txt.index(' ')+1):])
	last = ''.join(list_txt[:list_txt.index(' ')])
	print(first, last, sep=' ')

name_shuffle("Donald Trump")
name_shuffle("Rosie O'Donnell")
name_shuffle("Seymour Butts")

# Example 2
words = []
def spin_words(sentence):
	name_split = sentence.split(' ')
	for term in name_split:
		if len(term) >= 5:
			y = list(term)[::-1]
			x = ''.join(y)
			words.append(x)
		else:
			words.append(term)

	print(' '.join(words))

spin_words("I would like to work for India and Myself")