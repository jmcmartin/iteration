# https://www.braceyourself.io/apcsp/transposition/
# https://tabs.ultimate-guitar.com/tab/scorpions/rock_you_like_a_hurricane_chords_668765?simplified=1

scale = ["A", "A#", "B", "C", "C#", "D", "d#", "E", "F", "F#", "G", "G#"]


def keyshift(scale, chord, movement):
	chord_key = scale.index(chord)
	transposed = scale[chord_key - movement]
	return transposed

def transpose_song(song_info, scale, movement):
	song_info += ' '
	word = ''
	split_list = []
	
	for i in range(len(song_info)):
		if song_info[i] != ',' and song_info[i] != '\n' and song_info != "''":
			word += song_info[i]
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
			if new_list[d - 1] not in scale:
				transposed += '\n'
				transposed += new_list[d]
			else:
				transposed += new_list[d]
		else:
			transposed += new_list[d]
			transposed += '\n'
	
	return transposed



song = """

[Verse]

E          C
It's early morning
    E         A
The sun comes out
     E         C
Last night was shaking
    E      A
And pretty loud
   E      C
My cat is purring
    E            A
And scratches my skin
   E       C
So what is wrong
  E       A
With another sin

    E        C
The bitch is hungry
    E        A
She needs to tell
   E        C
So give her inches


    E        A
And feed her well

     E       C
More days to come
    E         A
New places to go
     E      C
I've got to leave
     E          A
It's time for a show


[Chorus]

E         G A    
Here I am,     
C            D       E         G A C D
Rock you like a hurricane
E         G A    
Here I am,     
C            D       E         G A C D C
Rock you like a hurricane


[Verse]

   E            C
My body is burning
   E           A
It starts to shout
E            C
Desire is coming
   E              A
It breaks out loud

E            C
Lust is in cages
           E                   A
Till the storm breaks loose
     E            C
Just have to make it
     E         A
With someone I choose

    E        C
The night is calling
  E       A
I have to go
    E       C
The wolf is hungry
   E       A
He runs to show

     E           C
He's licking his lips
     E        A
He's ready to win
       E    C
On the hunt tonight
    E             A
For love at first sting


[Chorus]

E         G A    
Here I am,     
C            D       E         G A C D
Rock you like a hurricane
E         G A    
Here I am,     
C            D       E         G A C D
Rock you like a hurricane 

"""


print transpose_song(song, scale, 2)