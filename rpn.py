#~/usr/bin/env python3

import operator
import random

def add(a,b):
	return a+b
def somefunction(a,b,c):
	return a*b*c
def whatever():
	return

ops = {
	'+':operator.add,
	'-':operator.sub,
	'^':operator.pow,
	'*':operator.mul, 
	'R':random.randint
}

def calculate(myarg):
	stack = list()
	for token in myarg.split():
#		if token == '+':
#			arg2 = stack.pop()
#			arg1 = stack.pop()
#			result = arg1+arg2
#			stack.append(result)
#		elif token == '-':
#			arg2 = stack.pop()
#			arg1 = stack.pop()
#			result = arg1-arg2
#			stack.append(result)
#		else:
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			function(arg1,arg2)
			result = function(arg1,arg2)
			stack.append(result)
	#print(stack)
	return stack.pop()

def main():
	while True:
		calculate(input("rpm calc> "))

if __name__ == '__main__':
	main()

