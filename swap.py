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

	#Alternate Method
def replace_letters(phrase, swapped_letter, final_letter):
	return phrase.replace(swapped_letter, final_letter)

print replace_letters("banana", "a", "!")


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

	#Alternate Method

def switch_letters2(phrase, swapped_letter_1, swapped_letter_2):
	return phrase.replace(swapped_letter_1, "!").replace(swapped_letter_2, "@").replace("!", swapped_letter_2).replace("@", swapped_letter_1)

print switch_letters2("textbook", "e", "o")



#Number 3



def switch_words(phrase, word1, word2):
	return phrase.replace(word1, "!").replace(word2, "$").replace("!", word2).replace("$", word1)

print switch_words("The quick brown fox jumps over the lazy dog", "fox", "dog")



#Number 4



list_of_censored_words = ["fuck", "shit", "ass", "bitch"]
replacement_words = ["heck", "poop", "butt", "friend"]

censored_phrase = []

def censor_text(phrase, bad_words, good_words):
	for i in phrase:
		if phrase[i: ] == list_of_censored_words:
			censored_phrase.append(replacement_words)

		else:
			censored_phrase.append(i)

	return censored_phrase

print censor_text("What the fuck is this shit you bitch ass", list_of_censored_words, replacement_words)