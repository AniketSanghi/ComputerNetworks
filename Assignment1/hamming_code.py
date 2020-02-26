import sys

def read_input():

    file = open("input.txt", "r")

    strings = [ string for string in file.read().split("\n") if len(string) > 0]

    file.close()
    return strings

def flip(a):
	if a == '0':
		return '1'
	else:
		return '0'

def nib(string):
	return string[2] + string[4] + string[5] + string[6]

def decode(para):

	if len(para)%14 != 0:
		print("INVALID", end = "")
		return

	nibbles = [para[i:i+7] for i in range(0, len(para), 7)]

	H = [[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]]
	H_cols = [4, 2, 6, 1, 5, 3, 7]
	errors = 0
	total = 0

	vals = []
	chars = ""

	for nibble in nibbles:

		val = 0
		for i in range(0,3):
			for j in range(0,7):
				val = val ^ (H[i][j] & int(nibble[j]))
			val = val<<1
		vals.append(val >> 1)

	for i in range(0, len(nibbles), 2):

		total += 1
		if vals[i] != 0 or vals[i+1] != 0:
			
			errors += 1
			if vals[i] != 0:
				ind = H_cols.index(vals[i])
				temp = list(nibbles[i])
				temp[ind] = flip(temp[ind])
				nibbles[i] = "".join(temp)
			if vals[i+1] != 0:
				ind = H_cols.index(vals[i+1])
				temp = list(nibbles[i+1])
				temp[ind] = flip(temp[ind])
				nibbles[i+1] = "".join(temp)
		chars = chars + chr(int(nib(nibbles[i]) + nib(nibbles[i+1]), 2))

	print(chars)
	print(int(errors*100/total), "%", end = "")


paras = read_input()

for i,para in enumerate(paras):
	
	decode(para)
	if i != len(paras) - 1:
		print("\n")
