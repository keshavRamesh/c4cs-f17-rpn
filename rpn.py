#~/usr/bin/env python3

import operator

def add(a,b):
	return a+b

ops = {
	'+':operator.add,
	'-':operator.sub,
	'^':operator.pow
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

