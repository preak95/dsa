import random
import helper as hp

"""====================== Sorting Algorithms ======================"""

def bubble_sort(unsorted_list):
	"""
	Worst case complexity: O(n^2)
	Best case complexity: O(n)
	"""

	flag = 1
	while flag:
		flag = 0
		for i in range(len(unsorted_list) - 1):
			if unsorted_list[i] > unsorted_list[i+1]:
					hp.swap(unsorted_list, i, i+1)
					flag = 1

	return unsorted_list

def selection_sort(unsorted_list):
	for position in range(len(unsorted_list)):
		for i in range(position + 1, len(unsorted_list)):
			# Find the minimum in this range and swap it with the current position 
			# if the found min is lesse than the current item at position
			minimum = hp.find_minimum(unsorted_list, i, len(unsorted_list)) 
			if minimum[0] < unsorted_list[position]:
				hp.swap(unsorted_list, position, minimum[1])

	return unsorted_list


def insertion_sort(unsorted_list):
	for i in range(1, len(unsorted_list)):
		for j in range(i):
			if unsorted_list[j] > unsorted_list[i]:
				# The jth item should be inserted in place i
				hp.insert(unsorted_list, j, i)
			else:
				pass
			print(unsorted_list)
	return unsorted_list



"""The Main function starts here"""

def main():
	unsorted_list = hp.get_unsorted_list()
	print(unsorted_list)
	sorted_list = insertion_sort(unsorted_list)

	print("\n ====== Sorted List ====== \n")
	print(sorted_list)



if __name__ == '__main__':
	main()
