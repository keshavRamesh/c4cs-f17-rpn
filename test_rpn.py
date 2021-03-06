import unittest

import rpn


class TestFunctions(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2,result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2,result)
	def test_power(self):
		result = rpn.calculate('4 2 ^')
		self.assertEqual(16,result)
	def test_random(self):
		result = rpn.calculate('1 100 R')
		if result <= 100 and result >= 1:
			self.assertEqual(1,1)
		else:
			self.assertEqual(1,0)
		
