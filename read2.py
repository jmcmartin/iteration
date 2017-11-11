#!/usr/bin/env python
import sys
import plotly
import plotly.graph_objs as go

data = open("cars.csv", "r")
lines = data.readlines()


#Number 0
list_of_makes_and_models_2006 = []
year_2006 = "2006"

def cars_2006(list_of_makes_and_models_2006):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")	

		if info[3] == year_2006:
			list_of_makes_and_models_2006.append(info[1])
			list_of_makes_and_models_2006.append(info[2])

	return list_of_makes_and_models_2006

print "~~~~~~"
print "List of all car makes and models from the year 2006:"
print cars_2006(list_of_makes_and_models_2006)
print "~~~~~~"


#Number 1


any_year_test = "1998"
any_year_list = []

def cars_any_year(any_year_list):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == any_year_test:
			any_year_list.append(info[1])
			any_year_list.append(info[2])

	return any_year_list

print "List of all makes and models from any given year:"
print cars_any_year(any_year_list)


#Number 2


toyotas_since_2000_years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"]
toyotas_list_since_2000 = []

def toyotas_2000(toyotas_list_since_2000):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		if info[3] == toyotas_since_2000_years and info[1] == "Toyota":
			toyotas_list_since_2000.append(info[1])
			toyotas_list_since_2000.append(info[2])
			toyotas_list_since_2000.append(info[3])
	
	return toyotas_list_since_2000

print "~~~~~~"
print "Toyotas in list since 2000:"
print toyotas(toyotas_list_since_2000)


#Number 3


print "~~~~~~"
print "Most popular color of car in the list:"

list_of_colors = []
color_counter = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")

	list_of_colors.append(info[4])


for color in list_of_colors:
	total = 0
	if list_of_colors[i] == color:
		total += 1

	color_counter.append(total)


def maximum(color_counter):
	current_max = color_counter[0]
	for n in color_counter:
		if n > current_max:
			current_max = n

	return current_max

print maximum(color_counter)

print "~~~~~~"

data = [go.Bar(
			x = list_of_colors,
			y = color_counter
	)]
plotly.offline.plot(data, filename='basic-bar')


"""favorite_movies = ["Star Wars", "Jaws", "Back to the Future", "The Avengers"]
votes = [12, 5, 15, 20]

data = [go.Bar(
			x = favorite_movies,
			y = votes
	)]
plotly.offline.plot(data, filename='basic-bar')"""
