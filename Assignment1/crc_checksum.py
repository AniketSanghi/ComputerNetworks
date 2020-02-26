import sys

def read_input(filename):

    file = open(filename, "r")

    contents = file.read()
    input_bytes = [contents[i:i+8] for i in range(0, len(contents), 8)]

    file.close()
    return input_bytes

def get_frames():

	indices_of_flag = [i for i, byte in enumerate(input_bytes) if byte == flag ]
	frames = []
	checksums = []
	for i in range(0, len(indices_of_flag), 2):
		frames.append(input_bytes[indices_of_flag[i]+1:indices_of_flag[i+1]-1])
		checksums.append(input_bytes[indices_of_flag[i+1]-1])
	return frames, checksums

def find_invalid_frames():

	invalid_frames = []
	generator = int("10000011", 2)
	for ind, frame in enumerate(frames):
		data = ''.join(frame) + "0000000"
		curr = int(data[0:8], 2)
		if curr >= 128:
			curr = curr ^ generator
		for bit in data[8:]:
			curr = (curr << 1) | int(bit, 2)
			if curr >= 128:
				curr = curr ^ generator
		if curr<<1 != int(checksums[ind], 2):
			invalid_frames.append(str(ind + 1))
	return invalid_frames

def find_valid_string():

	string = ""
	for i, frame in enumerate(frames):
		if str(i+1) not in invalid_frames:
			prev = ""
			for byte in frame:
				if prev == ESC:
					string = string + chr(int(byte, 2) ^ 32)
					prev = byte
				elif byte == ESC:
					prev = ESC
				else:
					string = string + chr(int(byte,2))
	return string


# Reading input from file
input_bytes = read_input(sys.argv[1])

# Declaring global constants
flag = "10101001"
ESC = "10100101"

# Get different frames and checksums
frames, checksums = get_frames()

print(len(frames))

invalid_frames = find_invalid_frames()

print(','.join(invalid_frames))

decoded_string = find_valid_string()

print(decoded_string, end = '')