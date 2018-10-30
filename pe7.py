#prime 10001
import numpy
import sys

debug = False

def primes_in_range(primes, start, upper = 1000, prime_set = None):
	
	#is prime = True, default to True, then switch to false via Sieve
	nums = numpy.full(shape = upper, fill_value = True, dtype = bool)
	
	if prime_set == None:
		prime_set = set(primes)
	
	for p in primes:
		p_start = p
		while p_start < start:
			p_start = p_start + p
		for mult in range(p_start, start + upper, p):
			nums[mult - start] = False
		for i in range(0, min(p**2 - start, upper)):
			if(nums[i] and i + start not in prime_set):
				primes.append(i + start)
				prime_set = prime_set.union({i + start})
	# if(debug):
		# print(primes)	
		# print(len(primes))
	return prime_set

def main(argv):
	find_nth_prime = -1
	try:
		find_nth_prime = int(argv[0])
	except ValueError:
		return -1
	
	primes = [2]
	start = 2
	upper = 1000
	prime_set = set(primes)
	
	debug = False
	while(len(primes) < find_nth_prime):
		prime_set = primes_in_range(primes, start, upper, prime_set)
		upper = upper * 2
		start = start + upper

	print(primes[find_nth_prime - 1])
	# print(prime_set)
	# for p in primes:
		# if p not in prime_set:
			# print("OOPS")
			# print(p)
			# print()
		
if __name__ == "__main__":
   main(sys.argv[1:])