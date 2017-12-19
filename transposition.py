# https://www.braceyourself.io/apcsp/transposition/
# https://tabs.ultimate-guitar.com/tab/foreigner/juke_box_hero_chords_1794057?simplified=1
# A Bb B C Db D Eb E F Gb G Ab
# A A# B C C# D d# E F F# G G#
def


def transpose_song(song_info, scale, movement):
	song_info += ' '
	word = ''
	split_list = []
	
	for i in range(len(song_info)):
		if song_info[i] != ',' and song_info[i] != '\n' and song_info != "''":
			wod += song_info[i]
		else:
			split_list.append(word)
			word = ''
			
	new_list = []
	for n in range(len(split_list)):
		if split_list[n] in scale:
			chord = keyshift(scale, split_list[n], movement)
			new_list.append(split_list[n])
		else:
			new_list.append(split_list[n])
	
	transposed = ""
	for d in range(len(new_list)):
		if new_list[d] in scale:
			if new_list[d-1] not in scale:
				transposed += '\n'
				transposed += new_list[d]
			else:
				transposed += new_list[d]
		else:
			transposed += new_list[d]
			transposed += '\n'
	return transposed


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
