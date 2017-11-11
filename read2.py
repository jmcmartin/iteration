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
print toyotas_2000(toyotas_list_since_2000)


#Number 3


print "~~~~~~"
print "Most popular color of car in the list:"

car_colors = []

def most_popular_color(car_colors):
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")

		car_colors.append(info[4])

	list_of_colors = []
	for i in range(0, car_colors):
		if car_colors[i] not in list_of_colors:
			list_of_colors.append(car_colors[i])
	
	color_counts = []
	for color in list_of_colors:
		total = 0
		for car_color in car_colors:
			if car_color == color:
				total += 1

		color_counts.append(total)


	def maximum(color_counts):
		current_max = color_counts[0]
		for n in color_counts:
			if n > current_max:
				current_max = n

		return current_max

	return maximum(color_counts)

print most_popular_color(car_colors)
print "~~~~~~"

data = [go.Bar(
			x = list_of_colors,
			y = color_counts
	)]
plotly.offline.plot(data, filename='basic-bar')


"""favorite_movies = ["Star Wars", "Jaws", "Back to the Future", "The Avengers"]
votes = [12, 5, 15, 20]

data = [go.Bar(
			x = favorite_movies,
			y = votes
	)]
plotly.offline.plot(data, filename='basic-bar')"""
