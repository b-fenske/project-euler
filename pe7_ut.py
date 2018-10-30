import pe7
import unittest

dir - '../primes/'
primes = ["primes-to-100k.txt", "primes-to-200k.txt", "primes-to-300k.txt"]

def read_file(file):
	with open(file) as f:
		return [x.strip() for x in f.readlines()]

#update naming in pe7, possibly extract out class
class test_prime_sieve(unittest.TestCase):
	
	
	primes_under_100k = []
	primes_under_200k = []
	primes_under_300k = []
	
	
	# sequence = ((5, 16),(16, 8), (8, 4), (4, 2), (2,1))
	# def test_next_in_sequence(self):
		# for input, output in self.sequence:
			# result = pe14.collatz(input)
			# self.assertEqual(result, output)

	def __init__(self, unittest.TestCase):
		#serialize? Add set for easy membership?
		primes_under_100k = read_file(primes[0])
		primes_under_200k = read_file(primes[1])
		primes_under_300k = read_file(primes[2])


if __name__ == '__main__':
	unittest.main()