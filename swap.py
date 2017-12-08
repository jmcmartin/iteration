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

#Split function to break up the original bad sentence
def split_sentence(first_sentence):
	first_sentence += ' '
	word = ''
	split_list = []

	for i in range(len(first_sentence)):
		if first_sentence[i] != ' ':
			word += first_sentence[i]

		else:
			split_list.append(word)
			word = ''

	return split_list


def switch_words(phrase, word1, word2):
	new_sentence = ""
	check_words = split_sentence(phrase)
	for i in range(len(check_words)):
		if check_words[i] == word1:
			new_sentence += word2
			new_sentence += ' '

		elif check_words[i] == word2:
			new_sentence += word1
			new_sentence += ' '

		else:
			new_sentence += check_words[i]
			new_sentence += ' '

	return new_sentence

print switch_words("The quick brown fox jumps over the lazy dog", "fox", "dog")



#Number 4
	

list_of_censored_words = ["fuck", "shit", "ass", "bitch"]
replacement_words = ["heck", "poop", "butt", "friend"]

def censor_text(bad_sentence):
	good_sentence = ""
	check_words = split_sentence(bad_sentence)
	for i in range(len(check_words)):
		if check_words[i] not in list_of_censored_words:
			good_sentence += check_words[i] + ' '
		for n in range(len(list_of_censored_words)):
			if check_words[i] == list_of_censored_words[n]:
				good_sentence += replacement_words[n] + ' '

	return good_sentence

	
print censor_text("What the fuck is this shit you bitch ass")