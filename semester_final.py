# Take list of bands and songs and find out how many songs of each band is in the playlist and how many times songs of the chosen band have been played
#!/usr/bin/env python
import sys

data = open("playlist.csv", "r")
lines = data.readlines()

list_of_bands = []
list_of_songs = []
number_of_plays = []


songs_of_requested_band = []

def songs_per_band(list_of_songs, requested_band):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[0] == requested_band:
			songs_of_requested_band.append(info[1])

	return songs_of_requested_band

print songs_per_band(list_of_songs, "Poison")

"""def times_band_was_played(list_of_songs, requested_band):"""