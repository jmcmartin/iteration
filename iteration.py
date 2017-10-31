# This is change [a] from home

# Make a change from home


# Make another local change

# Make a local change

# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

"""def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item


def add_one(list):
	for i in range(0, len(list)):
		list[i] += 1

	return list


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total

def maximum(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

#Homework due for 10/26/17

def average(scores):
	total = 0
	for n in scores:
		total += n

	return total / len(scores)

def average_without_bottom_two_scores(scores):
    current_min = scores[0]
  	
  	for n in scores:
        if n <= current_min:
            current_min = n
    
    current_min2 = scores[0]

    for n in scores:
        if n <= current_min2:
            current_min2 = n
    
    sum_without_bottom_two_scores = 0
    
    for n in scores:
        sum_without_bottom_two_scores += n

    return (sum_without_bottom_two_scores - current_min - currentmin2) / len(scores)"""

#In class 10/27/17

"""def alternating_sum(numbers):
	total = numbers[0]
	for i in range(1, len(numbers)):
		if i % 2 == 0:
			total += numbers[i]
		else:
			total -= numbers[i]

	return total


def sum_outside(numbers):
	total = 0
	for n in numbers:
		if not (min <= n and n < max):
			total += n 

	return total
		

def count_close_remainders(numbers2):
	divisor = 5
	
	count = 0

	for n in numbers2:
		remainder = n % divisor
		if remainder <= 1 or remainder == divisor-1:
			count += 1

	return count


def double_down(numbers3):
	target_integer = 6

	previous_integer = n - 1
	# Negative numbers to show position from the right
	close_integers = [-1, -2, -3]

	for n in numbers3:
		if n > previous_integer:
			n * 2

		elif n = close_integers"""

def standard_deviation(heights):
	total = 0
	for n in heights:
		total += n

	mean1 = total % n

	for n in heights:
		(n - mean1) * (n - mean1)

	total_final = 0
	for n in heights:
		total_final += n

	mean2 = total_final % n

	return mean2