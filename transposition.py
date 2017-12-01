# https://www.braceyourself.io/apcsp/transposition/
# https://tabs.ultimate-guitar.com/tab/led_zeppelin/stairway_to_heaven_chords_46450
# A Bb B C Db D Eb E F Gb G Ab
# A A# B C C# D d# E F F# G G#


scale = ["A", "A#", "B", "C", "C#", "D", "d#", "E", "F", "F#", "G", "G#"]
verse1 = "There's a feeling I get,"
verse2 = "When I look to the West."
verse3 = "And my spirit is crying for leaving."
verse4 = "In my thoughts I have seen,"
verse5 = "Rings of smoke through the trees,"
verse6 = "And the voices of those who stand looking."

def move_down_two(note, scale):
	position_of_note = scale.index(note)
	final_note = scale[(position_of_note - 2)]
	return final_note

print move_down_two("A#", scale)
print verse1
print " "
print move_down_two("A", scale)
print verse2
print " "
print move_down_two("A", scale), move_down_two("F", scale)
print verse3
print " "
print move_down_two("A", scale)
print verse4
print " "
print move_down_two("A", scale)
print verse5
print " "
print move_down_two("A", scale), move_down_two("F", scale)
print verse6