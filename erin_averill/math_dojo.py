# Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:
# x = md.add(2).add(2,5,1).subtract(3,2).result
# print(x) # should print 5

# which should perform 0+2+(2+5+1)-(3+2) and print 5.

class MathDojo(object):
	def __init__(self):
		self.value = 0

	def add(self, *numbers):
		for number in numbers:
			if type(number) == list or type(number) == tuple:
				for numeral in number:
					self.value += eral
			else:
				self.value += arg
		return self
	def subtract(self, *numbers):
		for number in numbers:
			if type(number) == list or type(number) == tuple:
				for numeral in number:
					self.value -= numeral
			else:
				self.value -= numeral
		return self
	def endResult(self):
		print(self.value)
		return self


		


maths = MathDojo()
maths.add(2).add(2,5).subtract(3,2).endResult()
# maths2.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).endResult()

# import the python testing framework
# import unittest
# our "unit"
# this is what we are running our test on
# def add(num1, *num):
# 	print(num1)
# 	print(num) # run this test with add(5,2,9,8) will print 5 and then (2,9,8)(is a tuple) for x in num: print(x) will print it into 2 9 5

# class Mathdojo(object):
#     def __init__(self):
#         self.value = 0
#     def add(self, *args):
#         for arg in args:
#             if type(arg) == list or type(arg) == tuple:
#                 for numeral in arg:
#                     self.value += numeral
#             else:
#                 self.value += arg
#         return self
#     def subtract(self, *args):
#         for arg in args:
#             if type(arg) == list or type(arg) == tuple:
#                 for numeral in arg:
#                     self.value -= numeral
#             else:
#                 self.value -= arg
#         return self
#     def result(self):
#         print(self.value)
#         return self

# md = Mathdojo()

# # md.add(2).add(2,5).subtract(3,2).result()
# md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).result()
