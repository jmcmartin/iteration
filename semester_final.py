# Take list of bands and songs and find out how many songs of each band is in the playlist and how many times songs of the chosen band have been played
#!/usr/bin/env python
import sys

data = open("playlist.csv", "r")
lines = data.readlines()

list_of_bands = []
list_of_songs = []

songs_of_requested_band = []

def split_sentence(first_sentence):
	first_sentence += ' '
	word = ''
	split_list = []

	for i in range(len(first_sentence)):
		if first_sentence[i] != ",":
			word += first_sentence[i]

		else:
			split_list.append(word)
			word = ''

	return split_list

def num_of_songs_and_bands():
	for i in range(1, len(lines)):
		info = split_sentence(lines[i])

		if info[0] not in list_of_bands:
			list_of_bands.append(info[0])
			
		if info[1] not in list_of_songs:
			list_of_songs.append(info[1])


	num_of_bands = len(list_of_bands)
	num_of_all_songs = len(list_of_songs)

	print "In your playlist, you have a total of", num_of_bands, "different bands and", num_of_all_songs, "different songs."


def songs_per_band(list_of_songs, requested_band):
	for i in range(1, len(lines)):
		info = split_sentence(lines[i])

		if info[0] == requested_band:
			songs_of_requested_band.append(info[1])

	num_of_songs = len(songs_of_requested_band)

	if num_of_songs == 1:
		print "You have", num_of_songs, "song from your favorite band called", requested_band, "which is:"
		return songs_of_requested_band

	else:
		print "You have", num_of_songs, "songs from your favorite band called", requested_band, "which are:"
		return songs_of_requested_band


def times_band_was_played(requested_band):
	total_times_played = 0

	for i in range(1, len(lines)):
		info = split_sentence(lines[i])

		if info[0] == requested_band:
			total_times_played == total_times_played + info[2]


	print "You have listened to your favorite band", requested_band, total_times_played, "times this year."



print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print " "
print "APCSP Final"
print " "
print " "
print num_of_songs_and_bands()
print " "
print " "
print songs_per_band(list_of_songs, "AC/DC")
print " "
print " "
print times_band_was_played("AC/DC")
print " "
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
