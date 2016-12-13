#!/usr/bin/python
# Performs a bubble sort, with built in test function if needed.
# Param: Array to sort - theArray.
# Param: Boolean Ascending - True/False
# Return: Returns a sorted array as defined.

def bubbleSort(theArray, ascending):
	# Assume we traverse the array at least once
	swap = True

	# Repeat the process until swap remains False
	while swap:
		# Swap defaults to true, to ensure the loop fires...
		# However, immediately set it to false to make sure subsequent for loop had to bubble an item
		swap = False
		# Check each array element versus the next item
		for i in range(len(theArray)-1):
			if ascending:
				if theArray[i] > theArray[(i+1)]:
					tmp = theArray[(i+1)]
					theArray[(i+1)] = theArray[i]
					theArray[i] = tmp
					swap = True # item bubbled
			else:
				# All that changes here is line 26, the > becomes <
				if theArray[i] < theArray[(i+1)]:
					tmp = theArray[(i+1)]
					theArray[(i+1)] = theArray[i]
					theArray[i] = tmp
					swap = True # item bubbled
	# The array should be sorted at this point
	return theArray

'''
# Test suite
print "Bubble Sort Test Suite"
print "-----------------------------------"
print "Test array:"

myArray = [0, 43, 11, 21, 32, 99, 34, 101, 5, 8, 76]

print myArray
print "Sorted Ascending: " + str(bubbleSort(myArray, True))
print "Sorted Descending: " + str(bubbleSort(myArray, False))
print "\n"

print "ASCII Test array:"

asciiArray = ["a", "f", "h", "z", "x"]

print asciiArray
print "Sorted Ascending: " + str(bubbleSort(asciiArray, True))
print "Sorted Descending: " + str(bubbleSort(asciiArray, False))
print "\n"

print "Complex ASCII Test array:"

complexArray = ["Apple", "Ardvark", "John", "Joe", "Zebra", "Marge", "Moxy", "Niagra", "Noob"]

print complexArray
print "Sorted Ascending: " + str(bubbleSort(complexArray, True))
print "Sorted Descending: " + str(bubbleSort(complexArray, False))
print "\n"
'''