
# What you learned
# You can call lists like example[":10"] where this says give me 10 index values from the start of the list [10:] would return from the end of the list. 

# What to understand better
# the set() function / module. And intersections. 


def gameInput(filename):
	file = open(filename)
	rucksacks = []
	for item in file:
		rucksacks.append(item)
	return rucksacks

def rucksackSplit(data):
	x = len(data) // 2
	compartment1 = data[:x]
	compartment2 = data[x:]
	return compartment1, compartment2

def commonItem(compartment1, compartment2):
	common = set(compartment1).intersection(set(compartment2))
	return list(common)

def itemPriority(item):
	alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	return alpha.index(item) + 1

def sumPriorities(items):
	total_priority = 0 
	for item in items:
		split = rucksackSplit(item)
		common = commonItem(split[0], split[1])
		priority = itemPriority(common[0])
		total_priority = total_priority + priority
	return total_priority


print(sumPriorities(gameInput('input.txt')))

