from tkinter import filedialog
import os
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def autorun_config():
    flag = True
    file_name = filedialog.askopenfilename(title="Select AUTORUN.INF in the base directory (root) of a removable drive",filetypes=[("AUTORUN.INF (you can choose other files but AUTORUN.INF is highly recommended)","*.inf")])
    if file_name[3:] != 'autorun.inf':
        input("File not in the root of a removable device! Please select AUTORUN.INF in the base folder (root) of your removable device or create it.\nPress ENTER to restart program")
        start()
    while flag == True:
        clear()
        print("AUTORUN Configurator - © Lan Internet Software")
        print(f"Current AUTORUN.FILE: {file_name}")
        print("[1] Change Drive Icon")
        print("[2] Configure startup file")
        print("[3] Change disk label")
        print("[4] Configure custom AutoPlay action")
        print("[5] Extra information")
        print("[6] Choose different file")
        print("[7] Reset file")
        print("[8] Quit")
        option = input("Enter an option: ")
        if option == "1" or option == "2" or option == "3":
            with open(file_name, "r") as output:
                feature_present = False
                feature_line = 0
                lines = output.readlines()
                for x in range(len(lines)):
                    if "icon" in lines[x] and option == "1":
                        feature_present = True
                        feature_line = x
                    if "open" in lines[x] and option == "2":
                        feature_present = True
                        feature_line = x
                    if "label" in lines[x] and option == "3":
                        feature_present = True
                        feature_line = x               
                if option == "1":         
                    new_icon = filedialog.askopenfilename(title="Select an icon",filetypes=[("Icon files","*.ico")])[2:]
                if option == "2":
                    startup_file = filedialog.askopenfilename(title="Select an file that will start upon the drive being plugged in",filetypes=[("Any file","*.*")])[2:]
                if option == "3":
                    label = input("Enter a new drive label: ")
                if feature_present == True:
                    if option == "1":
                        lines[feature_line] = f"icon = {new_icon}"
                    if option == "2":
                        lines[feature_line] = f"open = {startup_file}"
                    if option == "3":
                        lines[feature_line] = f"label = {label}"
                    output.close()
                else:
                    if option == "1":
                        lines.append(f"icon = {new_icon}")
                    if option == "2":
                        lines.append(f"open = {startup_file}")
                    if option == "3":
                        lines.append(f"label = {label}")
                    output.close()
            with open(file_name, "w") as writing:
                print("The current file is being written do. This may take several minutes. Do not unplug the device or modify any files during this process")
                for x in range(len(lines)):
                    writing.writelines(lines[x] + '\n')
                input("The file has been successfully saved. To see the effects, you must unplug and re-plug your removable disk, so make sure no files are opened on the disk and use the Safe Eject option whenever possible\nPress ENTER to return to main menu...")
        if option == "4":
            with open(file_name, "r", encoding='ansi') as output:
                lines = output.readlines()
                output.close()
            temp = lines.copy()
            tempflag = [False, False]
            valid = ["A", "B"]
            option = input("[A] Add or change action\n[B] Remove action")
            if option not in valid:
                input(f"Invalid option - {option}. Valid options are 'A' or 'B'!\nPress ENTER to return to main menu...")
            else:
                action_name = input("Enter the internal name of your action (technical name): ")
                if option == 'A':
                    user_name = input("Enter a short description of the action (e.g View README): ")
                    action = filedialog.askopenfilename(title="Select an file that will start upon the action being selected",filetypes=[("Any file","*.*")])[2:]
                    for x in range(len(temp)):
                        if f'shell\\{action_name}' in temp[x] and f'shell\\{action_name}\\command' not in temp[x]:
                            temp[x] = f"shell\\{action_name}={user_name}"
                            tempflag[0] = True
                        if f'shell\\{action_name}\\command' in lines[x]:
                            temp[x] = f'shell\\{action_name}\\command={action}'
                            tempflag[1] = True
                    if False in tempflag:
                        lines.append(f"shell\\{action_name}={user_name}")
                        lines.append(f'shell\\{action_name}\\command={action}')
                    else:
                        lines = temp
                with open(file_name, "w", encoding='ansi') as test:
                    print("The current file is being written do. This may take several minutes. Do not unplug the device or modify any files during this process")
                    for x in range(len(lines)):
                        test.writelines(lines[x] + '\n')
                    input("The file has been successfully saved. To see the effects, you must unplug and re-plug your removable disk, so make sure no files are opened on the disk and use the Safe Eject option whenever possible.\nPress ENTER to return to main menu...")
        if option == "5":
            clear()
            print("AUTORUN CONFIGURATION PROGRAM INFORMATIONS")
            print("This program is a rather short and simple program designed to configure your USB drives however you want. I use the AUTORUN.INF method as it is the simplest and the easiest for me.\nYou can select a new icon for your drive, you can make a startup file, meaning that it will start every time you plug in your removable device as well as correctly change the disk label and having custom AutoPlay actions.")
            input("Press ENTER to return to main menu...")
        if option == "6":
            start()
        if option == "7":
            with open(file_name, "w", encoding='ansi') as reset:
                reset.write("; Made by Lan Internet Software\n")
                reset.write("[autorun]\n")
            input("Reset successful. Press ENTER to continue")
        if option == "8":
            flag = False
            exit()
def start():
    if os.name != 'nt':
        input("WARNING!!! Program is not compatible with this operating system. Continuing may lead to unexpected behaviour!\nPress ENTER to start the program, CTRL-C to terminate the program")
    try:
        autorun_config()
    except KeyboardInterrupt:
        print("User has chosen to exit. Exiting...")
        exit()
    except Exception as e:
        print(f"An error has occured in this program. Review the GitHub GamerSoft24/Software PySoft error chart and the Python Manual for more information.\nError details: {e}")
        input("Press ENTER to RESTART this program, CTRL-C to terminate this program")
        start()
start()
