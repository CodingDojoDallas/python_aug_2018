# Countdown - Create a function that accepts a number as an input.  Return a new array that counts down by one, from the number 
#(as arrays 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].

def countDown(number):
	newArr = []
	while number >= 0:
		newArr.append(number)
		number = number - 1
	return newArr

countDown(5)

# Print and Return - Your function will receive an array with two numbers. Print the first value, and return the second.

def printReturn(arr):
	print(arr[0])
	return(arr[1])

printReturn([1,2])

# First Plus Length - Given an array, return the sum of the first value in the array, plus the array's length.

def firstPlus(arr):
	for i in arr:
		arr[i] = arr[i] + len(arr)
	return arr
# Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are
# greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return False

def valueGreaterThanSecond (anyArr):
	sum = 0
	for i in anyArr:
		if anyArr[i] > anyArr[i+1]:
			sum = sum + 1
			print sum
		if sum < 1:
			return "False"

# This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size and value. This function 
#should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) 
#should return [7,7,7,7].

