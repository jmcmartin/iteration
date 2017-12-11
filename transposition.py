# https://www.braceyourself.io/apcsp/transposition/
# https://tabs.ultimate-guitar.com/tab/whitesnake/is_this_love_chords_1397497
# A Bb B C Db D Eb E F Gb G Ab
# A A# B C C# D d# E F F# G G#


scale = ["A", "A#", "B", "C", "C#", "D", "d#", "E", "F", "F#", "G", "G#"]

verse1 = ["Is this love", "C", 2]
verse2 = ["that I'm feeling", "D", 2]
verse3 = ["Is this the love,", "B", 2]
verse4 = ["that I've been searching for", "C", "B", "A", 2]
verse5 = ["Is it love", "C", 2]
verse6 = ["or am I dreaming?", "D", "F", 2]
verse7 = ["This must be love", "B", 2]
verse8 = ["Cause it really,", "C", 2]
verse9 = ["got a hold on me,", "B", "A", "G", 2]
verse10 = ["a hold on me...", "F", 2]

def transpose(note, scale, value_up_or_down):
	position_of_note = scale.index(note)
	final_note = scale[(position_of_note - value_up_or_down)]
	return final_note

print transpose(verse1[1], scale, verse1[2])
print verse1[0]
print " "
print transpose(verse2[1], scale, verse2[2])
print verse2[0]
print " "
print transpose(verse3[1], scale, verse3[2])
print verse3[0]
print " "
print transpose(verse4[1], scale, verse4[4]), transpose(verse4[2], scale, verse4[4]), transpose(verse4[3], scale, verse4[4])
print verse4[0]
print " "
print transpose(verse5[1], scale, verse5[2])
print verse5[0]
print " "
print transpose(verse6[1], scale, verse6[3]), transpose(verse6[2], scale, verse6[3])
print verse6[0]
print " "
print transpose(verse7[1], scale, verse7[2])
print verse7[0]
print " "
print transpose(verse8[1], scale, verse8[2])
print verse8[0]
print " "
print transpose(verse9[1], scale, verse9[4]), transpose(verse9[2], scale, verse9[4]), transpose(verse9[3], scale, verse9[4])
print verse9[0]
print " "
print transpose(verse10[1], scale, verse10[2])
print verse10[0]
