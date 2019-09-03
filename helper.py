import random

"""====================== Helper Functions ======================"""

def get_unique_random_number(unsorted_list, size):
	# Returns a unique random number which isn't already present in list
	random_num = random.randint(0,size)
	if random_num in unsorted_list:
		return get_unique_random_number(unsorted_list, size)
	else:
		return random_num

def get_unsorted_list(size):
	# Create a list of "size" random numbers between 0-1000
	random_list = []
	for i in range(0, size):
		random_num = get_unique_random_number(random_list, size)
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

def merge_lists(list1, list2):
	i = j = k = 0
	merged_list = [0] * ((len(list1) + len(list2)))
	"""
	This part of merging will stop as soon as one of i, j reaches
	the middle or the end respectively. See next, comment.
	"""
	while i < len(list1) and j < len(list2):
		if list1[i] < list2[j]:
			merged_list[k] = list1[i]
			i += 1
		else:
			merged_list[k] = list2[j]
			j += 1
		k += 1

	# Now, for the remaining elements, you have to just traverse 
	# and put them into the list

	while i < len(list1):
		merged_list[k] = list1[i]
		i += 1
		k += 1

	while j < len(list2):
		merged_list[k] = list2[j]
		j += 1
		k += 1

	return merged_list