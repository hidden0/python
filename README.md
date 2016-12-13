# Python Library
Defines a routine set of functions for handling data structures, file I/O, as well as threading in a Python script.

## How to use
- Ensure the `lib/` folder is inside your python project.
- Load the library via `import lib`
- Access methods as such:

   - Bubble Sort:		lib.bubbleSort.bSort(array,sortOrder)
   - Binary Search:	lib.binarySearch.binSearch(array,target,sortOrder)

- Tests can be ran by appending "Test" to the end of the function with no parameters:

   - Bubble Sort:		lib.bubbleSort.bSortTest()
   - Binary Search:	lib.binarySearch.binSearchTest()

## Library
- [bubbleSort.py](lib/bubbleSort.py)

   This function will sort any form of array, and has a built in test suite to validate output to observe the results.
   ToDo: Describe expected behavior, paramaters, and return output. Usage.
- [binarySearch.py](lib/binarySearch.py)

   A function to take an already sorted array and perform a binary search for a given value. Works on most data types.
   ToDo: Describe expected behavior, paramaters, and return output. Usage.
