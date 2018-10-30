import pe14
import unittest

class test_collatz(unittest.TestCase):
	sequence = ((5, 16),(16, 8), (8, 4), (4, 2), (2,1))
	
	def test_next_in_sequence(self):
		for input, output in self.sequence:
			result = pe14.collatz(input)
			self.assertEqual(result, output)

if __name__ == '__main__':
	unittest.main()