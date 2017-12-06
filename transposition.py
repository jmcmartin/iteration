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

def move_down_two(note, scale):
	position_of_note = scale.index(note)
	final_note = scale[(position_of_note - 2)]
	return final_note

print move_down_two("C", scale)
print verse1
print " "
print move_down_two("D", scale)
print verse2
print " "
print move_down_two("B", scale)
print verse3
print " "
print move_down_two("C", scale), move_down_two("B", scale), move_down_two("A", scale)
print verse4
print " "
print move_down_two("C", scale)
print verse5
print " "
print move_down_two("D", scale), move_down_two("F", scale)
print verse6
print " "
print move_down_two("B", scale)
print verse7
print " "
print move_down_two("C", scale)
print verse8
print " "
print move_down_two("B", scale), move_down_two("A", scale), move_down_two("G", scale)
print verse9
print " "
print move_down_two("F", scale)
print verse10