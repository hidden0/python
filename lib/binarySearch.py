#!/usr/bin/python
'''
Description:	Issues a binary search on the array. A binary search will only be successful
				if the provided array is already sorted (such as with [bubbleSort.py](lib/bubbleSort.py))

Param: 			Array to sort - theArray.
Param:			Target to hit (value) - target
Param: 			Boolean Ascending - True/False. Decides search direction logic (test suite shows expected behavior)
Return: 		Returns the index of the value being searched for within the array.
				Say the target value is at index 5, the value returned will be 5.
				If the target value is not found in the array, a value of None will be returned.

Author:			Johnathan Thorne
Date:			12/12/16
'''

def binarySearch(theArray, target, ascending):
	answer = None
	space = len(theArray)
	sIndex = int(round(space / 2))
	diffTrack = space - sIndex

	# Pointer starts in the middle of the array, and we assume no answer is to be found at the start
	while diffTrack > 1:
		tmp = diffTrack
		if ascending:
			if theArray[sIndex] == target:
				answer = sIndex
				break
			elif theArray[sIndex] > target:
				# Reduce sIndex to search downard
				sIndex -= int(round(diffTrack / 2))
				diffTrack -= int(round(tmp / 2))
			elif theArray[sIndex] < target:
				# Increase sIndex to search upward
				sIndex += int(round(diffTrack / 2))
				diffTrack -= int(round(tmp / 2))
		else:
			if theArray[sIndex] == target:
				answer = sIndex
				break
			elif theArray[sIndex] < target:
				# Reduce sIndex to search downard
				sIndex -= int(round(diffTrack / 2))
				diffTrack -= int(round(tmp / 2))
			elif theArray[sIndex] > target:
				# Increase sIndex to search upward
				sIndex += int(round(diffTrack / 2))
				diffTrack -= int(round(tmp / 2))

	return answer

''' # Test suite
import bubbleSort # needed to sort the array [bubbleSort.py](lib/bubbleSort.py)

print "Binary Sort Test Suite"
print "-----------------------------------"
print "Test array:"

myArray = [0, 43, 11, 21, 32, 99, 34, 101, 5, 8, 76, 4]

print myArray
print "Sorted Ascending: " + str(bubbleSort.bSort(myArray, True))
print "Sorted Descending: " + str(bubbleSort.bSort(myArray, False))
print "Ascending search for 43: " + str(binarySearch(bubbleSort.bSort(myArray, True), 43, True))
print "Descending search for 43: " + str(binarySearch(bubbleSort.bSort(myArray, False), 43, False))

print "ASCII Test array:"

asciiArray = ["a", "f", "h", "z", "x"]

print asciiArray
print "Sorted Ascending: " + str(bubbleSort.bSort(asciiArray, True))
print "Sorted Descending: " + str(bubbleSort.bSort(asciiArray, False))
print "Ascending search for 'x': " + str(binarySearch(bubbleSort.bSort(asciiArray, True), "x", True))
print "Descending search for 'x': " + str(binarySearch(bubbleSort.bSort(asciiArray, False), "x", False))
print "\n"

print "Complex ASCII Test array:"

complexArray = ["Apple", "Ardvark", "John", "Joe", "Zebra", "Marge", "Moxy", "Niagra", "Noob"]

print complexArray
print "Sorted Ascending: " + str(bubbleSort.bSort(complexArray, True))
print "Sorted Descending: " + str(bubbleSort.bSort(complexArray, False))
print "Ascending search for 'Moxy': " + str(binarySearch(bubbleSort.bSort(complexArray, True), "Moxy", True))
print "Descending search for 'Moxy': " + str(binarySearch(bubbleSort.bSort(complexArray, False), "Moxy", False))
print "\n"

print "Mixed ASCII Test array:"

mixedArray = ["1Apple", "0Ardvark", "5John", "4Joe", "Zebra3", "9Marge", "9Moxy", "0Marge", "0Moxy", "7Niagra", "1Noob3"]

print mixedArray
print "Sorted Ascending: " + str(bubbleSort.bSort(mixedArray, True))
print "Sorted Descending: " + str(bubbleSort.bSort(mixedArray, False))
print "Ascending search for '9Moxy': " + str(binarySearch(bubbleSort.bSort(mixedArray, True), "9Moxy", True))
print "Descending search for '9Moxy': " + str(binarySearch(bubbleSort.bSort(mixedArray, False), "9Moxy", False))
print "\n"
'''