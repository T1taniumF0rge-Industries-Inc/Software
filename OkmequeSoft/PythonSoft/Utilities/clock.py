import time #not the most efficient algorithm, on low end computers CPU usage may be high. This is to ensure accuracy of the time
while True:
	print(str(time.asctime()),end='\r')
