def collatz(cur):
	if cur % 2 == 0:
		return cur // 2
	return 3*cur + 1

seq = []
dict = {}
longest = (-1, 0)
debug = True
#1000001
for i in range(1, 11):
	if dict.get(i) == None:
		seq = [i]
		cur = i
		while(dict.get(cur) == None and cur != 1):
			cur = collatz(cur)
			seq.append(cur)
		
		#cache hit. 
		if(dict.get(cur) != None):
			length = dict.get(cur) + len(seq) - 1
			if(length > longest[0]):
				longest = (length, i)
		#if dict.get(i) != None:
		#	for j in range(1, len(seq)):
		#		dict[seq[-j]] = length - (seq[len] + j
		else:
			dict[i] = len(seq)
		if debug:
			print(seq)
			print(longest)
			print()
if debug:
	print(dict)

#print("The longest sequence is: " + longest)

bob = [0, 1, 2]
for i in range(0, len(bob)-1):
	print(bob[i])
	
	
	#{4 [1} 3 ]