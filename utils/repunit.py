def repunit(k):
	if k < 0:
		raise ValueError('Let k be a whole number')
	out = 0
	for i in range(k):
		out += 10**i
	return out

