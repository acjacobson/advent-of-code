def scanSignal(signal, scan_size):
	signal_length = len(signal)
	start = 0 
	end = start + scan_size
	while start <= (signal_length - scan_size):
		if len(set(signal[start:end])) == scan_size:
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
print(scanSignal(signal, 14))