pe8 = "pe8.txt"
adjacent = 4 

greatest = 0
mult = 1

f = open(pe8, "r")
digits = f.read()

for i in range(len(digits) - adjacent):
	for j in digits[i : i + adjacent]:
		mult = mult * int(j)
	if mult > greatest:
		greatest = mult
	mult = 1
print(greatest)
