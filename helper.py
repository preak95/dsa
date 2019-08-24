import random

"""====================== Helper Functions ======================"""

def get_unique_random_number(unsorted_list):
	# Returns a unique random number which isn't already present in list
	random_num = random.randint(0,10)
	if random_num in unsorted_list:
		return get_unique_random_number(unsorted_list)
	else:
		return random_num

def get_unsorted_list():
	# Create a list of 100 random numbers between 0-1000
	random_list = []
	for i in range(0, 10):
		random_num = get_unique_random_number(random_list)
		random_list.append(random_num)

	return random_list

def swap(unsorted_list, i, j):
	temp = unsorted_list[i]
	unsorted_list[i] = unsorted_list[j]
	unsorted_list[j] = temp

def insert(list_l, new_index, current_index):
	item = list_l[current_index]
	temp_i = current_index - 1
	while temp_i >= new_index:
		list_l[temp_i + 1] = list_l[temp_i]
		temp_i -= 1
	list_l[new_index] = item

	return list_l

def find_minimum(unsorted_list, i, j):
	# This function assumes the minimum in list to be greaater than -1
	minimum = 100000
	min_index = -1
	for x in range(i, j):
		if unsorted_list[x] < minimum:
			minimum = unsorted_list[x]
			min_index = x
	return minimum, min_index