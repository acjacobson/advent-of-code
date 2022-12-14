def parseStacks(filename, start, end):
	f = open(filename, 'r')
	parse = f.readlines()
	lines = []
	for i in range(start, end):
		parse[i] = parse[i].replace('\n','')
		parse[i] = parse[i].replace('    ', '[0]')
		parse[i] = parse[i].replace(' ', '')
		parse[i] = parse[i].replace('][', ',')
		parse[i] = parse[i].replace(']', '')
		parse[i] = parse[i].replace('[', '')
		parse[i] = parse[i].split(',')	
		lines.append(parse[i])
	stack = []
	for n in range(0,len(lines) + 1):
		stack.append([])
	for item in lines:
		for n in range(0,len(lines) + 1):
			stack[n].append(item[n])
	for item in stack:
		for n in range(0,len(stack)):
			try:
				item.remove('0')
			except:
				continue 
	return(stack)

def parseMoves(filename, start, end):
	f = open(filename, 'r')
	parse = f.readlines()
	moves = []
	for i in range (start, end):
		parse[i] = parse[i].replace('\n','')
		parse[i] = parse[i].replace('move ','')
		parse[i] = parse[i].replace(' from ',',')
		parse[i] = parse[i].replace(' to ',',')
		parse[i] = parse[i].split(',')
		moves.append(parse[i])
	return moves

def sortCargo(count, start, end):
	stack = shipment[start-1][:count]
	stack.reverse()
	for i in stack:
		shipment[end - 1].insert(0, i)
	del shipment[start-1][:count]
	
shipment = parseStacks("input.txt", 0, 8)
moves = parseMoves("input.txt", 10, 512)

for item in moves:
	count = int(item[0])
	start = int(item[1])
	end = int(item[2])
	sortCargo(count, start, end)

top = ''
for item in shipment:
	try:
		top = top + item[0]
	except:
		continue

print(top)




