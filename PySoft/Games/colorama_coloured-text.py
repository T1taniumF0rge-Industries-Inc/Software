
try:
    import colorama
    from colorama import *
    import time
    import random
    import os
    import msvcrt
except (ImportError, ModuleNotFoundError) as e: # Error codes, descriptions and solutions can be found at https://github.com/GamerSoft24/Software/blob/Main/PySoft/Errors%20chart.md
    print(f"STOP: 1002/1099\nCannot import required modules, module contains an error or module is not found. Make sure all dependencies are installed as per the GitHub GamerSoft24/Software PySoft requirements.txt file, and try again.\nDetails: {e}")
    input("Press ENTER to EXIT...")
    exit()
except Exception as e:
    print(f"Failed to start program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python manual for more info.\nDetails: {e}")
init() # Colorama Initialisation
global colours
global backgrounds
global colour1 # Main lists of colours
colours = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN,  Fore.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.RED]
backgrounds = [Back.BLACK, Back.BLUE, Back.CYAN, Back.GREEN,  Back.LIGHTBLACK_EX, Back.LIGHTCYAN_EX, Back.LIGHTMAGENTA_EX, Back.LIGHTRED_EX, Back.LIGHTWHITE_EX, Back.RED]
colour1 = [ Fore.BLACK, Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN,  Fore.LIGHTBLACK_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, Fore.RED]
def clear(): # Clear Screen
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def printer(text, iterations = 10, background_colour = 1, foreground_colour = 1, mode = 0) -> None: # Main printing function
    global colours
    global backgrounds
    global colour1
    clear()
    print(f"Current mode selected: {mode + 2}")
    for x in range(iterations):
        for y in range(10):
            if mode == 0:
                print(random.choice(backgrounds) + random.choice(colours) + text + Fore.RESET + Back.RESET, end='\r')
            elif mode == 1:
                print(backgrounds[background_colour] + random.choice(colours) + text + Fore.RESET + Back.RESET, end='\r')
            elif mode == 2:
                print(random.choice(backgrounds) + random.choice(colours) + text + Fore.RESET + Back.RESET, end='\r')
            elif mode == 3:
                print(backgrounds[y] + colour1[y] + text + Fore.RESET + Back.RESET, end='\r')
            elif mode == 4:
                print(backgrounds[background_colour] + colours[y] + text + Fore.RESET + Back.RESET, end='\r')
            elif mode == 5:
                print(backgrounds[y] + colours[foreground_colour] + text + Fore.RESET + Back.RESET, end='\r')
            time.sleep(0.1)
    input("Press ENTER to continue...")
    return
def list_modes(): # Lists available colours according to the colours and backgrounds list
    print("[0] Black")
    print("[1] Blue")
    print("[2] Light Blue")
    print("[3] Green")
    print("[4] Grey")
    print("[5] Cyan")
    print("[6] Light Magenta")
    print("[7] Light Red")
    print("[8] Light White")
    print("[9] Red")
while True:
    try:
        clear() # Line below resets all terminal colours
        print(Fore.RESET + Back.RESET + "*** COLOURAMA COLOURED TEXT TESTER***") # Colour is the correct spelling if you live in the UK. If you live in the US, deal with the fact that British people exist
        print("[1] Demonstration of available modes")
        print("[2] Random background and foreground")
        print("[3] Fixed background, random foreground")
        print("[4] Fixed foreground, random background")
        print("[5] Cycling foreground and background")
        print("[6] Fixed background, cycling foreground")
        print("[7] Fixed foreground, cycling background")
        print("[8] Configurator mode")
        print("[9] Exit")
        option = input("Select an option: ")
        if option == '1':
            demo = 'This text is used to demonstrate the different operating modes of this program. '
            printer(demo, mode=0)
            printer(demo, mode=1)
            printer(demo, mode=2)
            printer(demo, mode=3)
            printer(demo, mode=4)
            printer(demo, mode=5)
        elif option in ("2","3","4","5","6","7"): #The most compact way to do this
            text = input("Enter text to display in your selected mode: ")
            iteration = int(input("Enter amount of iterations (1 iteration ≈ 1.1 seconds)"))
            foreground_selection = 0
            background_selection = 0 
            if option == "4" or option == "7":
                list_modes()
                foreground_selection = int(input("Select foreground/text colour: "))
            if option == "3" or option == "6":
                list_modes()
                background_selection = int(input("Select background colour: "))
            printer(text, mode=int(option) - 2, foreground_colour=foreground_selection, background_colour=background_selection, iterations=iteration)
        elif option == "8":
            string = ''
            string += Fore.WHITE
            string += Back.BLACK
            while True:
                clear()
                print(f'Result: {string}')
                print(Fore.RESET + Back.RESET + "Press ENTER to configure text or exit") # Reset colours here as well so that no colours leak
                character = msvcrt.getwch() # Fancy Input function using msvcrt
                if character == '\x08' and len(string) > 0:
                    string = string[:-1]
                elif character == '\r':
                    string += Fore.RESET
                    string += Back.RESET
                    user_exit = input(Fore.RESET + Back.RESET + "Exit?[Y/N]: ")
                    if user_exit == "Y":
                        break
                    list_modes()
                    foreground_selection = int(input("Select foreground/text colour: "))
                    background_selection = int(input("Select background colour: "))
                    string += colours[foreground_selection]
                    string += backgrounds[background_selection]
                else:
                    string += character
        elif option == "9":
            exit()
    except ValueError as e:
        print(Fore.RESET, Back.RESET)
        print(f"STOP : 0211\nInvalid value was specified. When asked for a value, enter the CORRECT values that are specified.\nDetails: {e}")
        input("Press ENTER to continue...")
        continue
    except Exception as e:
        print(Fore.RESET, Back.RESET)
        print(f"STOP : 770A\nUnhandled exception has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python manual for more info.\Details: {e}")
        input("Press ENTER to continue...")
        continue
