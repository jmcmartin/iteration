#Number 1

new_phrase = []

def replace_letter(phrase, swapped_letter, final_letter):
	for i in phrase:
		if swapped_letter == i:
			new_phrase.append(final_letter)

		else:
			new_phrase.append(i)

	return new_phrase


print replace_letter("banana", "a", "!")


#Number 2

new_phrase2 = []

def switch_letters(phrase, swapped_letter_1, swapped_letter_2):
	for i in phrase:
		if swapped_letter_1 == i:
			new_phrase2.append(swapped_letter_2)

		elif swapped_letter_2 == i:
			new_phrase2.append(swapped_letter_1)

		else:
			new_phrase2.append(i)

	return new_phrase2

print switch_letters("textbook", "e", "o")


#Number 3

new_phrase3 = []

def switch_words(phrase, word1, word2):
	


print switch_words("The quick brown fox jumps over the lazy dog", "fox", "dog")