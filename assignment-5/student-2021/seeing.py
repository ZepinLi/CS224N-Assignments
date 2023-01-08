

with open('wiki.txt', 'r') as f:
	data = f.readlines()
	for _, line in zip(range(10), data):
		print(line)