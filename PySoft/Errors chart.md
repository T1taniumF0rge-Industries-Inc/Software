# Errors chart

## Please note that this chart will only be useful if we have built-in error handling systems in our programs!
***© Okmeque1 Corporation: [`/Okmeque1/software`](https://github.com/Okmeque1/software/blob/main/PythonSoft/errors.md)***

**6510A FileExistsError:** A file that exists is conflicting with the specified file file name. Delete the conflicting file.

**6510B FileNotFoundError:** The program could not find the specified file. Make sure the spelling and format is correct or create the specified file and try again.

**6510C:** Drive is read-only. Check permissions and try again.

**0280 SyntaxError:** The program you got has an error or has been tampered with. Open an issue or a pull request if you can fix it.

**0281 Exception:** The program you got has an error or has been tampered with. Open an issue or a pull request if you can fix it.

**0211 ValueError:** You have entered an incorrect value (e.g abc when asked for a numer) or the program you got has an error or an unspecified error with file has bad permissions. Make sure that you have entered the correct valus for what was asked (e.g 5 when asked for number) otherwise check permissions and try again, else contact support.

**0271 OSError:** Operating system error. Check your drive and program, as well as any files and try again.

**0272 IOError:** I/O ports error. A device on your system has either malfunctioned or has been unplugged.

**0251 TypeError:** The program you got has an error or has been tampered with. Open an issue or a pull request if you can fix it.

**0210 PermissionError:** Access violation in file or the file is being used by another process. Check permissions and try again.

**0250 EOFError:** Possible input fault or code has been tampered with. When ready to input command, press enter. Else contact support.

**0270 KeyboardInterrupt:** User has chosen to exit. No action is needed, and this can be ignored.

**0273 NameError:** The program you got has an error or an invalid reference was put in. Try again, else contact support.

**0253 ImportError:** Required module does not exist. Consult the [requirements.txt](/PySoft/Requirements.txt) for the list of required modules and install via 'pip' for best compatability. After installing try again. To save time, use `pip install -r requirements.txt` in the same directory where you downloaded the requirements.txt file to install all of the required modules

**0255 ZeroDivisionError:** Operation resulted from dividing by 0(invalid). Check parameters and what you have entered and try again

**755F RuntimeError:** Bad Python interpreter. Reinstall Python and try again (you might have a broken hard drive).

**760F SystemError:** Bad Python interpreter. Reinstall Python and try again (you might have a broken hard drive).

**765E MemoryError:** No more memory (consider upgrading your computer). Close all programs, then reboot and try again. If there's a bluescreen, just go on Ali Express, Temu or Ebay while your PC is rebooting and buy some more RAM sticks. 

**780F TimeOutError:** Operation took to long. Try again. (causes could be out of RAM, slow HDD or internet and more)

**770A GeneralException:** A general exception has occured, which means nothing and that a part of the program has had an exception. Try again and open an issue if problems persist.

**0261/0F0A:** Multiple errors have succeded at once,and since handlers can only handle 1 error, program crashes.Contact support.

**0199 ImportError:** Required module does not exist. Consult the [requirements.txt](/PySoft/Requirements.txt) for the list of required modules and install via 'pip' for best compatability. After installing try again. To save time, use `pip install -r requirements.txt` in the same directory where you downloaded the requirements.txt file to install all of the required modules

**0190 KeyError:** Either bad key was specified for accessing a dictionary internally or bad value was inputted(this is because programs map for example "T" to "True" and so for the dictionary side it would look like this dictest = {"T":"True"} and this : test = dictest[test]. So if you enter a "T" it works because it converts "T" to "True". But if you put in an "A", that doesn't exist in dictest which then produces error 0190). Try again and input the CORRECT values that are demanded.

**0910 IndexError:** Bad access value was specified in code or bad value was inputted(this because list looks like this : lst = [1,2,3] and so if you want to access the number 2 you do lst[1] but if you access lst[123] it won't exist and throws error 0910)

**1E/08 requests.exceptions.ConnectionError:** Module REQUESTS cannot access the specified website. Please check your cabling, wifi and if that does not work, contact the website administrator fore more info.

**1E/10 UnicodeDecodeError:** The specified encoder was unable to parse and return the file or string specified. Please use the other encoder available(if you used ANSI, try using UTF-8)

**1E/18 LookupError:** The encoder you specified does not exist. Please use either UTF-8 or ANSI.

**1E/20 tkinter.TclError:** The GUI application you have downloaded has been tampered with. Only download Okmeque1 code from Okmeque1/Software or GamerSoft24/Software. Contact Support.

**1E/21 urllib.error.URLError:** Like the Minecraft errors, this is a client-side error or server-side error. Errors like "An existing connection was forcibly closed by the remote host" indicate a server-side error. "Connection reset" means that the specified URL has been blocked by an administrator. Contact the owner of the site to resolve this issue

**1002 ModuleNotFoundError:** Required module does not exist. Consult the [requirements.txt](/PySoft/Requirements.txt) for the list of required modules and install via 'pip' for best compatability. After installing try again. To save time, use `pip install -r requirements.txt` in the same directory where you downloaded the requirements.txt file to install all of the required modules

**2124 NotImplementedError:** A feature is not implemented. Use alternative feature if possible
