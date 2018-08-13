# Basic - Print all the numbers/integers from 0 to 150.
def print():
	for number in range(1, 151):
	    print(number)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
def multiple():
	for number in range(5,1000001):
	    if number %5 == 0:
	        print(number)

# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. 
# If by 10, also print " Dojo".
def counting():
	for number in range(1, 100):
	    if number %10 == 5:
	        print('Coding')
	    elif number %10 == 0:
	        print('Dojo')
	    else:
	        print(number)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
def huge():
	sum = 0
	for number in range(0, 500000):
		if number %2 == 1:
			sum = sum + number
	print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).
def countdown():
	for number in range(2018, 0, -4):
		print(number)
# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, 
# print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
def flexCountdown(lowNum, highNum, mult):
	for number in range(lowNum, highNum + 1):
		if number is %mult == 0:
			print(number)