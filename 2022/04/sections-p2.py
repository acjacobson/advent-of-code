
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

# Check if pairs overlap
def pairCheck(s1, e1, s2, e2):
    if s1 <= s2 and e1 >= e2:
        return 1
    if s2 <= s1 and e2 >= e1:
        return 1
    if s1 >= s2 and s1 <= e2:
        return 1
    if e1 >= s2 and e1 <= e2:
        return 1
    else:
        return 0

# Process the full file 
def processPairs(filename):
    x = gameInput(filename)
    count = 0
    for item in x:
        check = pairCheck(item[0],item[1],item[2],item[3])
        if check == 1:
            count += 1
    return count

print(processPairs("input.txt"))
