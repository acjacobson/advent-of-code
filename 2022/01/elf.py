file = open("input.txt")

item_total = 0 
elves = []

for item in file:
	if item != '\n':
		item_total = item_total + int(item)
	if item == '\n':
		elves.append(item_total)
		item_total = 0 

elves.sort(reverse=True)

top3 = elves[0] + elves[1] + elves[2]

print (top3)

