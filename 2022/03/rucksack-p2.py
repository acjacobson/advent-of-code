
# Parse input data into a list (one item per line)
def gameInput(filename):
	file = open(filename)
	rucksacks = []
	for item in file:
		item = item.strip()
		rucksacks.append(item)
	return rucksacks

# Chunk list into groups of 3 
def groupRucksacks(rucksacks):
	n = 0
	grouped_rucksacks = [] 
	while n < len(rucksacks):
		grouped_rucksacks.append(rucksacks[n:n+3])
		n += 3
	return grouped_rucksacks

# Find common character between three list elements
def commonBadge(group):
	badge = set(group[0]).intersection(set(group[1])
		.intersection(set(group[2])))
	return list(badge)

# Assign priority per character
def itemPriority(item):
	alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return alpha.index(item) + 1

# Sum priorities from given list of characters
def sumPriorities(items):
	total_priority = 0 
	for item in items:
		common = commonBadge(item)
		priority = itemPriority(common[0])
		total_priority = total_priority + priority
	return total_priority

# String it all together 
def crunchData(filename):
	rucksacks = gameInput(filename)
	chunks = groupRucksacks(rucksacks)
	return sumPriorities(chunks)

print(crunchData("input.txt"))