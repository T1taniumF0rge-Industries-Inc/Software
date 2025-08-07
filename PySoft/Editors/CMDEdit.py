import msvcrt, os
global text
text = ""
file_name = ""
def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')
def find_replace(tofind, toreplace=None, parameter=False):
    global text
    splits = text.split('\n') # Split for every line using \n
    success = False # used for if there are no matches
    for x in range(len(splits)):
        pointer = 0 # String index pointer
        temp = 0 # temporary value, used to prevent infinite loops in one line
        while True:
            position = splits[x][pointer:].find(tofind) # Find value in one line starting from the pointer value
            if position == -1: # No match scenario
                break
            if temp > position: # Prevents infinite loops
                break
            pointer = position + 1 # increase pointer by 1 to skip last match
            temp = position # set temp to current position, used to prevent infinite loops
            input(f"Found at line {x}, position {position}. Press ENTER to continue...")
            success = True
    if success is not True:
        input("No matches found. Press ENTER to continue...")
    if parameter is True:
        text = text.replace(tofind, toreplace)
while True:
    try:
        clear()
        print("CMDEdit Text Editor - © Okmeque1 Software")
        print(text)
        print("CTRL-S = Save current loaded file, CTRL-E = Save as, CTRL-X = Load, CTRL-F = Find, CTRL-G = Find/Replace, CTRL-Z = Exit")
        character = msvcrt.getwch()
        if character == '\x08' and len(text) > 0: #Backspace and text delete
            text = text[:-1]
        elif character == '\r':
            text += '\n'
        elif character == '\x05': # CTRL-E, use for saving in a different file
            file_name = input("\nPlease enter a file name (A:\directory\subdirectory if on Windows, /dev/sda/folder on most other systems.). Full path must be specified if the file is not in the same directory as this program: ")
            with open(file_name, "w") as save:
                save.write(text)
            input("File saved. Press ENTER to continue...")
        elif character == "\x13": # CTRL-S, save to current file if loaded
            with open(file_name, "w") as save:
                save.write(text)
            input("File saved. Press ENTER to continue.")
        elif character == '\x18': # CTRL-X, use for loading
            file_name = input("\nPlease enter a valid file name (A:\directory\subdirectory if on Windows, /dev/sda/folder on most other systems.). Full path must be specified if the file is not in the same directory as this program: ")
            with open(file_name, "r") as load:
                text = load.read()
        elif character == '\x06': # CTRL-F, use for finding
            find = input("\nEnter thing to find in current editor: ")
            find_replace(find)           
        elif character == '\x07': # CTRL-G because apparently CTRL-H also maps to backspace because Windows legacy reasons???
            find = input("\nEnter thing to replace in current editor: ")
            replace = input("Enter replacement thing: ")
            find_replace(find, toreplace = replace, parameter=True)
        elif character == '\x1a': # CTRL-Z for EXITING.
            exit()
        else:
            text += character
    except FileNotFoundError as e: # Error codes are part of the GitHub GamerSoft24/Software PySoft errors chart. 
        print(f"STOP: 6510B\nCannot find the specified file. Make sure that the file you specified is a valid file and that it is spelled correctly.\nDetails: {e}")
        input("Press ENTER to continue...")
        continue
    except FileExistsError as e:
        print(f"STOP: 6510A\nThe file that you specified is conflicting with another file. Delete the conflicting file, choose a different name for your file or rename the conflicting file.\nDetails: {e}")
        input("Press ENTER to continue...")
        continue
    except Exception as e:
        print(f"STOP: 770A\nAn error has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python Manual for more info.\nDetails: {e}")
        input("Press ENTER to continue...")
        continue