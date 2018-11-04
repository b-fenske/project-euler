def gcd(a, b):
	if a < 0 or b < 0:
		raise ValueError('Please pass whole numbers')
		#flush out catches, code defensively
	
	
	
	if a == b:
		return a
	if a > b:
		return gcd(a - b, b)
	return gcd(a, b - a)

