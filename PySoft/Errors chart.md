# Errors chart

## Please note that this chart will only be useful if we have built-in error handling systems in our programs!
***© Okmeque1 Corporation: [`/Okmeque1/software`](https://github.com/Okmeque1/software/blob/main/PythonSoft/errors.md)***

**Before creating a GitHub issue or e-mail, please make sure to consult this document as well as the Python manual or documentation online. This will save you and us time.**

**6510A FileExistsError:** A file that already exists is conflicting with the specified file name. Delete or rename the conflicting file, or specify a different file name.

**6510B FileNotFoundError:** The program could not find the specified file. Make sure the spelling and format is correct or create the specified file and try again.

**0280 SyntaxError:** The program you got has an error or has been tampered with. Open an issue or a pull request if you can fix it.

**0281 Exception:** The program you got has an error or has been tampered with. Open an issue or a pull request if you can fix it.

**0211 ValueError:** You have entered an incorrect value (e.g "abc" when asked for a number) or the program you got has an error or an unspecified error with file has bad permissions. Make sure that you have entered the correct values for what was asked (e.g 5 when asked for number) otherwise check permissions and try again, else contact support.

**0271 OSError:** Operating system error. Check your system drive and program, as well as any files that were in use and try again.

**0272 IOError:** I/O ports error. A device on your system has either malfunctioned or has been unplugged, or a file operation has failed. Make sure that you can use any files that you specify, as well as making sure that all hardware is securely connected (like plugging in your USB drive all the way)

**0251 TypeError:** The program you got has an error or has been tampered with. Open an issue or a pull request if you can fix it.

**0210/6510C PermissionError:** Access violation in file or the file is being used by another process. Check permissions and try again.

**0250 EOFError:** Possible input fault or code has been tampered with. When ready to input command, press enter. Else contact support.  (note that most programs will not display errors and this can be used as an alternative method to exit, so if the program displays `User has chosen to exit. Exiting...`, it can be ignored.)

**0270 KeyboardInterrupt:** User has chosen to exit. No action is needed, and this can be ignored.

**0273/05HG NameError:** The program you got has an error or an invalid reference was put in. Try again, else contact support.

**0253 ImportError OR 1002 ModuleNotFoundError or 0199:** Required module does not exist or contains an error. Consult the [requirements.txt](/PySoft/requirements.txt) for the list of required modules and install via 'pip' for best compatability. After installing try again. To save time, use `pip install -r requirements.txt` in the same directory where you downloaded the requirements.txt file to install all of the required modules, See the [PySoft README](/PySoft/README.md) for more information on how to install modules

**0255 ZeroDivisionError:** Operation resulted from dividing by 0 (invalid). Check parameters and what you have entered and try again.

**755F RuntimeError:** Bad Python interpreter. Reinstall Python and try again (you might have a broken hard drive).

**760F SystemError:** Bad Python interpreter. Reinstall Python and try again (you might have a broken hard drive).

**765E MemoryError:** No more memory (consider upgrading your computer). Close all programs, then reboot and try again. If there's a bluescreen or it continues to fail, just go on Ali Express, Amazon or eBay while your PC is rebooting and buy some more RAM sticks. 

**780F TimeOutError:** Operation took too long. Try again. (causes could be out of RAM, slow HDD or internet and more.)

**770A GeneralException:** A general exception has occured, which means nothing and that a part of the program has had an exception. Try again and open an issue if problems persist.

**0261/0F0A:** Multiple errors have succeded at once, and since handlers can only handle 1 error, program crashes. Contact support.

**0190 KeyError:** Either bad key was specified for accessing a dictionary internally or bad value was inputted. Example:
```py
option = input("Is 2+2=5? [T/F]: ")
mapping = {"T":True, "F", False}
option = mapping[option] # Converts str "T" into boolean True. 
```
In the example shown, if the user enters 'G' for example, 'G' does not exist in the dictionary `mapping`, so the program will throw error 0190. Try again and input the CORRECT values that are demanded.

**0910 IndexError:** Bad access value was specified in code or bad value was inputted. Example:
```py
example = [1,2,3]
example[5] # Throws error 0910
```
In this example, the `example[5]` piece of code fails because index 5 does not exist in the list `example`, only indexes 0, 1 and 2 exist. Try again and input the CORRECT values that are demanded

**1E/08 requests.exceptions.ConnectionError:** Module `REQUESTS` cannot access the specified website. Please check your cabling, wifi and if that does not work, contact the website administrator for more info.

**1E/10 UnicodeDecodeError:** The specified encoder was unable to parse and return the file or string specified. Please use another encoder that is available (if you used ANSI, try using UTF-8).

**1E/18 LookupError:** The encoder you specified does not exist. Please use either UTF-8 or ANSI.

**1E/20 tkinter.TclError:** The GUI application you have downloaded has been tampered with. Only download Okmeque1 code from Okmeque1/Software or GamerSoft24/Software. Contact Support.

**1E/21 urllib.error.URLError:** Like the Minecraft errors, this is a client-side error or server-side error. Errors like "An existing connection was forcibly closed by the remote host" indicate a server-side error. "Connection reset" means that the specified URL has been blocked by an administrator. Contact the owner of the site to resolve this issue

**2124 NotImplementedError:** A feature is not implemented. Use alternative feature if possible.
