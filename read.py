#!/usr/bin/env python
import sys

data = open("animals.csv", "r")
lines = data.readlines()

animal_names = []
animal_ratings = []
animal_countries = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")

	animal_names.append(info[0])
	animal_ratings.append(info[1])
	animal_countries.append(info[2])

for row in range(0, len(animal_names)):
	print animal_names[row], " is rated ", animal_ratings[row], " and is liked most in ", animal_countries[row]

