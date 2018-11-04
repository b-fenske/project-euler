import gcd_euclid
import unittest

class test_gcd(unittest.TestCase):
	gcds = ((5, 4, 1), (10, 5, 5))
	transitive = ((48, 18, 6), (18, 48, 6))

	def test_gcds(self):
		for a, b, out in self.gcds:
			result = gcd_euclid.gcd(a, b)
			self.assertEqual(result, out)
	
	def test_gcd_transitive(self):
		for a, b, out in self.transitive:
			result = gcd_euclid.gcd(a, b)
			self.assertEqual(result, out)

if __name__ == '__main__':
	unittest.main()
