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

def gap_sort(unsorted_list, gap):
	for i in range(len(unsorted_list)):
		if i + gap < len(unsorted_list):
			if unsorted_list[i] > unsorted_list[i+int(gap)]:
				hp.swap(unsorted_list, i, i + int(gap))

def shell_sort(unsorted_list):
	gap = int(len(unsorted_list) / 2)
	gap = len(unsorted_list) - 1
	while gap > 0:
		gap_sort(unsorted_list, gap)
		print("Gap: " + str(gap) + " " + str(unsorted_list))
		gap = int (gap / 2)

	return unsorted_list

def merge_sort(unsorted_list):
	if len(unsorted_list) > 1:
		#print(len(unsorted_list))
		middle = len(unsorted_list) // 2
		#print("Middle: " + str(middle))
		left_half = unsorted_list[:middle]
		right_half = unsorted_list[middle:]

		print("------------------------------------------------------")
		print("Sorting: " + str(left_half) + "			" + str(right_half))
		merge_sort(left_half)
		merge_sort(right_half)

		print("Merging: " + str(left_half) + "			" + str(right_half))
		print("------------------------------------------------------")

		i = j = k = 0

		"""
		This part of merging will stop as soon as one of i, j reaches
		the middle or the end respectively. See next, comment.
		"""
		while i < len(left_half) and j < len(right_half):
			if left_half[i] < right_half[j]:
				unsorted_list[k] = left_half[i]
				i += 1
			else:
				unsorted_list[k] = right_half[j]
				j += 1
			k += 1

		# Now, for the remaining elements, you have to just traverse 
		# and put them into the list

		while i < len(left_half):
			unsorted_list[k] = left_half[i]
			i += 1
			k += 1

		while j < len(right_half):
			unsorted_list[k] = right_half[j]
			j += 1
			k += 1

		return unsorted_list



"""The Main function starts here"""

def main():
	unsorted_list = hp.get_unsorted_list(13	)
	print(unsorted_list)
	#unsorted_list = [2, 3, 1, 5, 0]
	sorted_list = merge_sort(unsorted_list)

	print("\n ====== Sorted List ====== \n")
	print(sorted_list)



if __name__ == '__main__':
	main()
