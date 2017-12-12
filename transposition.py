# https://www.braceyourself.io/apcsp/transposition/
# https://tabs.ultimate-guitar.com/tab/foreigner/juke_box_hero_chords_1794057?simplified=1
# A Bb B C Db D Eb E F Gb G Ab
# A A# B C C# D d# E F F# G G#


"""scale = ["A", "A#", "B", "C", "C#", "D", "d#", "E", "F", "F#", "G", "G#"]

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
"""


lyrics_and_cords_original = """   E
1. Standing in the rain with his head hung low.
                                         D  
Couldn't get a ticket, it was a sold out show.
                      E                           D  
Heard the roar of the crowd, he could picture the scene.
                   E                        D  
Put his ear to the wall, and like a distant scream.
                E                   D
He heard one guitar, just blew him away.
                 E                       D
Saw stars in his eyes and the very next day.

                    E                           D  
2. Bought a beat up six-string in a second hand store.
                   E                        D  
Didn't know how to play it but he knew for sure.
                 E                    D
That that one guitar felt good in his hands.
            E            D
Didn't take long to understand.
            E                   D
Just one guitar, slung way down low.
              E                       D
Was a one way ticket, only one way to go.

Bridge:
              B
So he started rocking, ain't never gonna stop.
              B
Gotta keep on rocking, someday he's gonna make it to the top.

Refr.:
         Em       G         D            Em
And be a juke box hero, got stars in his eyes.
       Em       G        D           Em
He's a juke box hero. He took one guitar
         G         D            Em
Juke box hero, saw stars in his eyes.
             G             D      E
Juke box hero, he'll come alive tonight.

                       E                    D  
3. In a town without a name, in a heavy downpour.
                          E                       D  
Thought he passed his own shadow by the backstage door.
                        E                     D  
Like a trip through the past, that day in the rain.
               E                    D  
That one guitar made his whole life change.

Bride
              B
So he started rocking, ain't never gonna stop.
              B
Gotta keep on rocking, someday he's gonna make it to the top.

Refr.:
         Em       G         D            Em
And be a juke box hero, got stars in his eyes.
       Em       G        D           Em
He's a juke box hero. He took one guitar
         G         D            Em
Juke box hero, saw stars in his eyes.
             G             D      E
Juke box hero, he'll come alive tonight.
"""