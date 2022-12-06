def testSuite():
	signal_1 = scanSignal('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
	signal_2 = scanSignal('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)
	signal_3 = scanSignal('nppdvjthqldpwncqszvftbrmjlhg', 4)
	signal_4 = scanSignal('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)
	signal_5 = scanSignal('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4)
	print(signal_1, signal_2, signal_3, signal_4, signal_5,)    

def duplicateCheck(segment):
	duplicates = [i for i in segment if segment.count(i) > 1]
	if len(duplicates) == 0:
		return 0 
	else:
		return 1 

def scanSignal(signal, scan_size):
	signal_length = len(signal)
	start = 0 
	end = start + scan_size
	while start <= (signal_length - scan_size):
		segment = duplicateCheck(signal[start:end])
		if segment == 0:
			return (start + scan_size)
			break
		else:	
			start += 1
			end += 1

def gameInput(filename):
	f = open(filename, 'r')
	signal = f.readlines()
	return signal[0]

signal = gameInput('input.txt')
print(scanSignal(signal, 4))

#testSuite()
