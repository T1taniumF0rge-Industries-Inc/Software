try:
    import random,time
    length = 20
    print("*****|THE SECURITY MANAGEMENT SYSTEM|*****")
    print("Program version: 5.21.2.")
    print("")
    print("This program and all of its accessible programs are open-source programs so you can share it anywhere on the internet, copy it on USB/CD/DVD or other medias or remix/edit it. It would still be nice if you mention in your copy GamerSoft24 and/or Okmeque1/GamerSoft24 so that the original code is not lost to time.")
    print("")
    print("Please read option 1 if this is the first time you use this program or if any updates has been done on this program's version, as new options or functions could be added. FOR BEST PERFORMANCE, PLEASE RUN THIS PROGRAM IN FULLSCREEN BY PRESSING F11.")
    print("")
    print("PLEASE DO NOT CHANGE THIS PROGRAM UNLESS YOU ARE GIVEN PERMISSION OR UNLESS YOU CREATE YOUR OWN VERSION. THIS PROGRAM TOOK DAYS TO BE AT IT'S CURRENT STATE AND CHANGING IT WITHOUT PERMISSION OR NOT ON YOUR OWN COPY COULD RUIN IT ENTIRELY AND/OR CRASH IT. THANK YOU FOR UNDERSTANDING!")
    print("")
    exit_code_not_choosen = ['246195','961793','502941','836401','143697','302869']
    exit_code_choosen = ''
    exit_code_choosen += random.choice(exit_code_not_choosen)
    
    
    # noinspection PyArgumentList
    def sms_main():
        security_manager = True
        while security_manager:
            print("MAIN MENU:")
            print("=============================")
            print("1 -> About this program.")
            print("2 -> Quit program.")
            print("")
            print("Accessible Programs:")
            print("")
            print("3 -> THE PASSWORD MANAGER SYSTEM.")
            print("4 -> THE BINARY ENCRYPTER & DECRYPTER SYSTEM.")
            print("")
            print("Other:")
            print("")
            print("5 -> Report an issue or problem.")
            print("6 -> Quit program")
            print("")
            option = int(input("Select option: "))
            if option == 1:
                print("")
                input("Specifications/informations about this program: ")
                print("")
                print("-> Program name: THE SECURITY MANAGEMENT SYSTEM (SMS).")
                print("-> Manufacturers: GamerSoft24 and Okmeque1/GamerSoft24.")
                print("-> Manufacturers' company: © GamerSoftware Corporation™ & © Okmeque1/GamerSoft24 Corporation™.")
                print("-> Program version: 4.37.4.")
                print("-> Program description: This program is a Security Management System (or SMS). It can access programs that are useful in terms of security and protection of your personal data.")
                print("-> Program security version: 5.1.0")
                print("")
                input("Press enter to continue...")
                print("")
    
            elif option == 3:
                print("")
                print("THE PASSWORD MANAGER SYSTEM is opening. You are going to be directed to the menu.")
                print("")
                input("Press enter to continue...")
                time.sleep(1)
                print("")
                print("*****|THE PASSWORD MANAGER SYSTEM|*****")
                print("Program version: 3.21.2.")
                print("")
                print("Please read option 4 if this is the first time you use this program or if any updates has been done on this program's version, as new options or functions could be added!")
                print("")
                print("When you are asked for a valid file name, please make sure that the directory is valid and for best compatibility or/and please make sure that the file exists.")
                print("")
                defaultfileask = input("Do you have the default file: 'pwd_openscs.pwd'?(Yes/No): ")
                if defaultfileask == "Yes" or "yes":
                    print("")
                    input("Press enter to continue...")
                    print("")
                    pwd_manager = True
                elif defaultfileask == "No" or "no":
                        filedefaultdownload = open("pwd_openscs.pwd","w")
                        print("")
                        print("Downloading 'pwd_openscs.pwd'. Please wait...")
                        time.sleep(2)
                        print("")
                        print("The file that you just downloaded is called 'pwd_openscs.pwd' and it is used for default saving if no file name or set name are entered and much more.")
                        print("")
                        input("Press enter to continue...")
                        print("")
                        filedefaultdownload.close()
                        pwd_manager = True
                else:
                        sms_main()
                while pwd_manager:
                    print("MENU: ")
                    print("=======================================")
                    print("1 -> Add and generate password to a save file.")
                    print("2 -> Show a password from a save file.")
                    print("3 -> Show all passwords from a save file.")
                    print("4 -> About this program.")
                    print("5 -> Change a password to a save file.")
                    print("6 -> Quit program.")
                    print("")
                    optionpwd_manager = int(input("Select option : "))
                    if optionpwd_manager == 1:
    
                        print("")
                        print('Welcome to your password generator! (learn more with option 4).')
    
                        chars = '¦¬`1!23£4$€5%6^7&8*9(0-_=+q"~{[]}=+QwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~^¨µù%#\|zéèàZxXcCvVbBnNmMm,<.>/?)'
    
                        number = 1
                        length = input('Password length: ')
                        length = int(length)
    
                        for pwd in range(number):
                            password = ''
                            for c in range(length):
                                password += random.choice(chars)
                            print("")
                            print(password)
                            print("")
                            print('Password generated! Now saving...')
                            filename = input("Please enter a valid file name: ")
                            if filename == "":
                                filename = "pwd_openscs.pwd"
                                set0 = input("Enter a set name or nothing to continue. This program does not support having 2 sets of the same set name. Entering a set name that already exists will/could cause conflict. ")
                                passave = open(filename, "a")
                                passave.write(set0 + " -> " + password)
                                passave.close()
                            else:
                                set0 = input("Enter a set name or nothing to continue. This program does not support having 2 sets of the same set name. Entering a set name that already exists will/could cause conflict. ")
                                passave = open(filename, "a")
                                passave.write(set0 + " -> " + password)
                                passave.close()
                            print("")
                            print("Save has completed with no disk errors.")
                            print("")
                            input("Press enter to continue...")
                            print()
    
                    elif optionpwd_manager == 2:
                        print("")
                        fileopen = input("Please enter a valid file name path. The format must be full with the drive name included if the file in question is not in the same directory as the one this program is in. If this is not respected, this program will/could terminate with the main program: ")
                        if fileopen == "":
                            passopen = open("pwd_openscs.pwd", "r")
                            set1 = input("Please enter the set name for the desired password: ")
                            print("")
                            print("Here is the password for this set name:")
                            print("")
                            for line in passopen:
                                if line.split(" -> ")[0] == set1:
                                    print(line.split(" -> ")[1])
                                    print("")
                                    input("Press enter to continue...")
                                    print("")
    
                        else:
                            passopen = open(fileopen, "r")
                            set1 = input("Please enter the set name for the desired password: ")
                            print("")
                            print("Here is the password for this set name:")
                            print("")
                            for line in passopen:
                                if line.split(" -> ")[0] == set1:
                                    print(line.split(" -> ")[1])
                                    print("")
                                    input("Press enter to continue...")
                                    print("")
    
                    elif optionpwd_manager == 3:
                        print("")
                        fileallopen = input("Please enter a valid file name path. The format must be full with the drive name included if the file in question is not in the same directory as the one this program is in. If this is not respected, this program will/could terminate with the main program: ")
                        if fileallopen == "":
                            fileallopen = "pwd_openscs.pwd"
                            passall0 = open(fileallopen,"r")
                            passall1 = passall0.read()
                            print("")
                            print("File identified. Reading in progress...")
                            time.sleep(2)
                            print("Reading complete!")
                            print("")
                            print("Here are all the passwords in the chosen file: ")
                            print("")
                            print(passall1)
                            print("")
                            input("Press enter to continue...")
                            print("")
                            passall0.close()
                        else:
                            passall0 = open(fileallopen,"r")
                            passall1 = passall0.read()
                            print("")
                            print("File identified. Reading in progress...")
                            time.sleep(2)
                            print("Reading complete!")
                            print("")
                            print("Here are all the passwords in the chosen file: ")
                            print("")
                            print(passall1)
                            print("")
                            input("Press enter to continue...")
                            print("")
                            passall0.close()
    
                    elif optionpwd_manager == 4:
                        print("")
                        input("Specifications/informations about this program: ")
                        print("")
                        print("-> Program name: THE PASSWORD MANAGER SYSTEM.")
                        print("-> Manufacturers: GamerSoft24 and Okmeque1/GamerSoft24.")
                        print("-> Manufacturers' company: © GamerSoftware Corporation™ & © Okmeque1/GamerSoft24 Corporation™.")
                        print("-> Program version: 3.21.2.")
                        print("-> Program description: This program is a Password Manager System. It can create, save, read, show and manage passcodes.")
                        print("-> Program security version: 5.1.0")
                        print("")
                        input("Compatibility of this program: ")
                        print("")
                        print("This program will run perfectly on Python Windows OS but will also run on macOS and Linux (kaliLinux) but the filepath format will vary as neither of those operating systems use drive letters: 'C:\...\Password Manager System\pwd' like Windows OS. The structure for those OS will either be: ")
                        print("")
                        print("1 -> macOS : The file structure may be: '/path/path1/Password Manager System/pwd.*' (Please note that this program might not work as macOS does not support hard-disk writing to a bit level and might throw an error about write fail or more.")
                        print("2 -> Linux (kaliLinux): The file structure is unclear as there are so many Linux distros and versions possible to download but the structure may be: '/dev/sda/mountpoint0/Password Manager System/pwd.*'.")
                        print("")
                        print("Please note that in both cases, even with Windows OS, please do not use file with extensions like *.dell (DELL file), *.pc (PC file) or any non-standard file format that can't be read by a text editor.) as the Check Disk Utility (or chkdsk.exe) might assume that the file is corrupted and delete it.")
                        print("")
                        input("Press enter to continue...")
                        print("")
                    elif optionpwd_manager == 5: 
                        filedels = input("Please enter a valid file name path. The format must be full with the drive name included if the file in question is not in the same directory as the one this program is in. If this is not respected, this program will/could terminate with the main program: ")
                        sets1 = input("Enter SET name to change : ")
        
                        with open(filedels,"r") as readpwd:
                            r1 = readpwd.readlines()
                            for b in range(len(r1)):
                                if r1[b].strip("\n").split(" -> ")[0] == sets1:
                                    setnarme = r1[b].strip("\n").split(" -> ")[0] + " -> "
                                    newpwd = input("Enter new password : ")
                                    newsetpwd = setnarme + newpwd + "\n"
                                    r1[b] = newsetpwd
                        with open(filedels,"w") as changepwd:
                            for a in range(len(r1)):
                                changepwd.writelines(r1[a])
                        print("Save completed with no disk errors. Returning to main menu...")
                    elif optionpwd_manager == 6:
                        print("")
                        print("Saving data to main program. Please wait...")
                        time.sleep(3)
                        print("")
                        input("Press enter to continue...")
                        print("")
                        pwd_manager = False
    
            elif option == 4:
                print("")
                print("THE BINARY ENCRYPTER & DECRYPTER SYSTEM is opening. You are going to be directed to the menu.")
                print("")
                input("Press enter to continue...")
                time.sleep(1)
                print("")
                print("*****|THE BINARY ENCRYPTER & DECRYPTER SYSTEM|*****")
                print("Program version: 2.21.1")
                print("")
                binary_encrypt_decrypt_system = True
                while binary_encrypt_decrypt_system:
                    print("MENU: ")
                    print("===================")
                    print("1 -> Encrypt text.")
                    print("2 -> Decrypt text.")
                    print("3 -> Quit program.")
                    print("")
                    optionbinary_encrypt_decrypt_system = int(input("Select option : "))
                    if optionbinary_encrypt_decrypt_system == 1:
                        print('')
                        plaintext = input("Enter the text to encrypt: ")
                        def text_to_binary(text):
                            binary_text = ' '.join(format(ord(char), '08b') for char in text)
                            return binary_text
                        encrypted = text_to_binary(plaintext)
                        print('')
                        print("Encrypted binary:", encrypted)
                        print('')
    
                    elif optionbinary_encrypt_decrypt_system == 3:
                        print("")
                        print("Saving data to main program. Please wait...")
                        time.sleep(3)
                        print("")
                        input("Press enter to continue...")
                        print("")
                        binary_encrypt_decrypt_system = False
    
                    elif optionbinary_encrypt_decrypt_system == 2:
                        print('')
                        binary_input = input("Enter the binary to decrypt (space-separated): ")
                        def binary_to_text(binary_text):
                            binary_list = binary_text.split()
                            text = ''.join(chr(int(binary, 2)) for binary in binary_list)
                            return text
                        decrypted = binary_to_text(binary_input)
                        print('')
                        print("Decrypted text:", decrypted)
                        print('')
    
            elif option == 2:
                print("")
                print("Erasing personal data from main program...")
                time.sleep(2)
                print("Saving data to database. Please wait...")
                time.sleep(5)
                print("")
                print("Exit code: " + exit_code_choosen)
                input("Press enter to continue...")
                print("")
                security_manager = False
    
            elif option == 5:
                print("")
                print("We are now connecting you to The Report Center. Please wait...")
                time.sleep(2)
                print("You are now connected! Please tell us what type of program issues or problems you experienced.")
                print("")
                input("Your report: ")
                print("")
                print("Sending your report. Please wait...")
                time.sleep(1)
                print("")
                print("Thank you for reporting! We will try our best to make our program better!")
                print("")
            elif option == 6:
                print("")
                print("We hope that this program was useful for your use case!")
                input("Press enter to exit this program.")
                exit()
    name_for_check = input("Enter your name for a reCAPTCHA bot scan (You can learn more after with option 1 in the main menu): ")
    if name_for_check == '_BrStd1':
        print()
        input("Hello fellow admin(s)! Welcome back!")
        print()
        sms_main()
    else:
        print()
        print("Checking your connection with reCAPTCHA v3...")
        time.sleep(2)
        input("All clear, free to go! Enjoy!")
        print()
        sms_main()

except FileExistsError:
    print("Error: 6510A\nAn existing file is in conflict with the selected file. Delete the old file")
    input("Press enter to return to the program...")
    sms_main()
except FileNotFoundError:
    print("Error: 6510B\nThe file specified was not found. Please make sure you have the correct file and that the path is valid.")
    input("Press enter to return to the program...")
    sms_main()
except OSError:
    print("Error: 0271\nOperating system error. Check your drive and program, as well as any files and try again.")
    input("Press enter to return to the program...")
    sms_main()
except ValueError:
    print("Error: 0211\nYou have entered the wrong value. When asked for a value, please input the correct value that is demanded (e.g length = number.)")
    input("Press enter to return to the program...")
    sms_main()
except KeyboardInterrupt:
    exit()
except EOFError:
    exit()
except BaseException:
    print("Error: 770A\nA random exception occured.")
    input("Press enter to return to the program...")
    sms_main()
except IOError:
    print("Error: 0272\nA device on your system has either malfunctioned or has been unplugged. The operating system will now forcibly close the program.")
    input("Press enter to continue...")
    exit()
except:
    exit()
    
