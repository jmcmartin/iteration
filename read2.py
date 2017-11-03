#!/usr/bin/env python
import sys

data = open("cars.csv", "r")
lines = data.readlines()

#Number 0
list_of_makes_and_models_2006 = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")

	if info[3] == "2006":
		list_of_makes_and_models_2006.append(info[1])
		list_of_makes_and_models_2006.append(info[2])


print "~~~~~~"
print "List of all car makes and models from the year 2006:"
print list_of_makes_and_models_2006
print "~~~~~~"

#Number 1
any_year_test = "1999"
any_year_list = []


for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")

	if info[3] == any_year_test:
		any_year_list.append(info[1])
		any_year_list.append(info[2])


print "List of all makes and models from any given year:"
print any_year_list

#Number 2

toyotas_since_2000_years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
toyotas_list_since_2000 = []

for i in range(1, len(lines)):
	info = lines[i].rstrip().split(",")

	if info[3] == toyotas_since_2000_years:
		toyotas_list_since_2000.append(info[1])
		toyotas_list_since_2000.append(info[2])

print "~~~~~~"
print "Toyotas in list since 2000:"
print toyotas_list_since_2000

#Number 3


print "~~~~~~"
print "Most popular color of car in the list:"

print "~~~~~~"