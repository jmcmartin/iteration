# https://www.braceyourself.io/apcsp/transposition/
# https://tabs.ultimate-guitar.com/tab/whitesnake/is_this_love_chords_1397497
# A Bb B C Db D Eb E F Gb G Ab
# A A# B C C# D d# E F F# G G#


scale = ["A", "A#", "B", "C", "C#", "D", "d#", "E", "F", "F#", "G", "G#"]

verse1 = "Is this love"
verse2 = "that I'm feeling"
verse3 = "Is this the love,"
verse4 = "that I've been searching for"
verse5 = "Is it love"
verse6 = "or am I dreaming?"
verse7 = "This must be love"
verse8 = "Cause it really,"
verse9 = "got a hold on me,"
verse10 = "a hold on me..."

def move_down_two(note, scale, value_up_or_down):
	position_of_note = scale.index(note)
	final_note = scale[(position_of_note - value_up_or_down)]
	return final_note

print move_down_two("C", scale, 2)
print verse1
print " "
print move_down_two("D", scale, 2)
print verse2
print " "
print move_down_two("B", scale, 2)
print verse3
print " "
print move_down_two("C", scale, 2), move_down_two("B", scale, 2), move_down_two("A", scale, 2)
print verse4
print " "
print move_down_two("C", scale, 2)
print verse5
print " "
print move_down_two("D", scale, 2), move_down_two("F", scale, 2)
print verse6
print " "
print move_down_two("B", scale, 2)
print verse7
print " "
print move_down_two("C", scale, 2)
print verse8
print " "
print move_down_two("B", scale, 2), move_down_two("A", scale, 2), move_down_two("G", scale, 2)
print verse9
print " "
print move_down_two("F", scale, 2)
print verse10