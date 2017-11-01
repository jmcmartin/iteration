#!/usr/bin/env python
import sys

data = open("cars.csv", "r")
lines = data.readlines()

makes_2006 = []
models_2006 = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")

	if info[3] == "2006":
		makes_2006.append(info[1])
		models_2006.append(info[2])


print makes_2006, models_2006

