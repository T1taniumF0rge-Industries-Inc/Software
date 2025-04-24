import time
import os
import winsound
input("To activate the alarm function, press CTRL-C. Press ENTER to activate the program...")
def almclock(alarm):
	print(f"The alarm will ring at {alarm}")
	try:
		while True:
			print(str(time.asctime()),end='\r')
			if time.asctime() == alarm:
				break
	except KeyboardInterrupt:
		print("                                           ")
		clearscreen()
		alarm += input("Enter a day. The format must be the first 3 letters of the day with the first letter a capitalized : ") + " "
		alarm += input("Enter a month. The format must be the first 3 letters of the month with the first letter capitalized : ") + " "
		fixbug = input("Enter a day from 01 to 30 or 31 depending on the month. The format must be with 2 digits. If the day is 0-9, you must type 09, 04, 01 and the rest you type it normally : ") + " "
		if fixbug[0] == '0':
			fixbug = ' ' + fixbug[1] + " "
		alarm += fixbug
		alarm += input("Enter an hour from 00 to 23. The format must be with 2 digits. If the hour is 00-09, you must type 00, 04, 09 and the rest you type it normally : ") + ":"
		alarm += input("Enter a minute from 00-59. The format must be with 2 digits. If the minute is 00-09, you must type it 00, 04, 09 and the rest you type it normally : ") + ":"
		alarm += input("Enter a second. Same rules as the minutes. If you don't know what that is then you can't read : ") + " "
		alarm += input("Enter a year : ")
		almclock(alarm)
		clearscreen()
	end()
def clearscreen():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
def end():
	if os.name == 'nt':
		while True:
			winsound.Beep(440,250)
			time.sleep(0.25)
almclock("")
