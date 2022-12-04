# Parse and format game input
def gameInput(filename):
	file = open(filename)
	pairs = []
	for item in file:
		x = item.replace('-',',')
		y = x.replace('\n','')
		pair = [int(z) for z in y.split(',')]
		pairs.append(pair)
	return pairs

# Check if any pair is inside another pair
def pairCheck(s1, e1, s2, e2):
	if s1 <= s2 and e1 >= e2:
		return 1
	if s2 <= s1 and e2 >= e1:
		return 1
	else: 
		return 0

def processFile(filename):
	x = gameInput(filename)
	count = 0
	for item in x:
		check = pairCheck(item[0],item[1],item[2],item[3])
		if check == 1:
			count += 1
		print(str(check) + str(item))
	return count

print(processFile("input.txt"))


