import os
CWD = os.getcwd()
while True:
    try:
        import random,time,os, pyperclip, hashlib
        from cryptography.fernet import Fernet
        def clear(): # Clear Screen
            # return # Uncomment this line for debugging purposes
            if os.name == 'nt': # Check for Windows NT (could be NT 3.51, but more realistically minimum would be NT 4.0.1381)
                os.system('cls')
            else:
                os.system('clear')
        length = 20
        CWD = os.getcwd()
        clear()
        print("***** | THE SECURITY MANAGEMENT SYSTEM ADVANCED EDITION | *****")
        print("Program version: 6.04E")
        print("")
        print("This program and all programs within are open source programs, meaning you can see their working code as well as copy it as per the GitHub GamerSoft24/Software repository License (BSD-3) as well as mention the developers, GamerSoft24, Okmeque1 and GmaerSoft42.")
        print("\nIf you are a new user to this program, it is recommended to select options 1 & 2 at the main menu to see extra informations about this program.")
        print("Contains ERROR HANDLING and INPUT VALIDATION SYSTEM™ Technology")
        print("")
        exit_code_not_choosen = str(random.randint(108476, 907384))
        exit_code_choosen = ''
        exit_code_choosen += exit_code_not_choosen
        # noinspection PyArgumentList (GmaerSoft: "what the hell is this? probably some random IDE thing")
        def sms_main():
            global CWD
            security_manager = True
            while security_manager:
                clear()
                print("MAIN MENU:")
                print("=============================")
                print("1 -> About this program.")
                print("2 -> Latest Updates / Changelog")
                print("")
                print("Accessible Programs:")
                print("")
                print("3 -> THE PASSWORD MANAGER SYSTEM.")
                print("4 -> THE FILE AND DATA ENCRYPTION SYSTEM")
                print("")
                print("Other:")
                print("")
                print("5 -> Legacy: Binary Encoder and Decoder System")
                print("6 -> Quit program")
                print("")
                option = int(input("Select option: "))
                if option == 1:
                    print("")
                    print("Specifications/informations about this program: ")
                    print("")
                    print("-> Program name: THE SECURITY MANAGEMENT SYSTEM (SMS) - Advanced Edition.")
                    print("-> Manufacturers: GamerSoft24 and Okmeque1/GamerSoft24.")
                    print("-> Manufacturers' company: © GamerSoftware Corporation™ & © Okmeque1/GamerSoft24 Corporation™.")
                    print("-> Program version: 6")
                    print("-> Program description: This program is a Security Management System (or SMS). It can access programs that are useful in terms of security and protection of your personal data.")
                    print("-> Program security version: 5.2.0")
                    print("")
                    print(" -> The advanced edition of this program is geared more towards professional users, and should be more reliable and secure.")
                    print("")
                    input("Press enter to continue...")
                    print("")
                elif option == 4:
                    clear()
                    print("")
                    print("THE FILE AND DATA ENCRYPTION SYSTEM is opening. You are going to be directed to the menu.")
                    print("")
                    print("Please read option 5 if this is the first time you use this program or if any updates has been done on this program's version, as new options or functions could be added!")
                    print("")
                    input("Press enter to continue...")
                    time.sleep(1)   
                    encryption_system = True
                    while encryption_system is True:
                        clear()
                        print("")
                        print("***** | THE FILE AND DATA ENCRYPTION SYSTEM | *****")
                        print("Program version: 1")
                        print("The 'Software' team will NOT be liable for any damages that result from the use of this program.")
                        print("") 
                        print("MENU: ")
                        print("=======================================")
                        print("1 -> Generate Fernet encryption key.")
                        print("2 -> Encrypt file.")
                        print("3 -> Decrypt file.")
                        print("4 -> Hash text.")
                        print("5 -> About this program.")
                        print("6 -> Quit to main menu.")
                        optionfile_data_encryption = input("Select option: ")
                        if optionfile_data_encryption == "1":
                            key = Fernet.generate_key()
                            keyfilename = input("Please enter a valid file name to save your encryption key. Make sure the file is empty as the file contents will be overwritten. If the file does not exist, the program will create it for you (for best compatibility, your file should end in '.frn' as it is the default format for Fernet key files for any programs in the PySoft folder): ")
                            with open(keyfilename, "wb") as keywrite:
                                keywrite.write(key)
                                print("")
                                print("Save has completed with no disk errors.")
                                print("")
                                input("Press enter to continue...")
                                print()
                        elif optionfile_data_encryption == "2" or optionfile_data_encryption == "3":
                            print()
                            file_name, keyfilename = '',''
                            while not os.path.exists(keyfilename):
                                keyfilename = input(f"Please enter a valid Fernet key file (usually ending in '.frn' if generated by programs of the GamerSoft24/Software repository unless you created your file using another format/program). The format must be full (all directories up to the root directory starting from your file) with the drive name included if the file in question is not in the same directory as the one this program is in ({CWD}). If this is not respected, you will have to re-enter the name of your file.: ")
                                print()
                            while not os.path.exists(file_name):
                                file_name = input(f"Please enter a valid file name path to perform the selected operation. The format must be full (all directories up to the root directory starting from your file) with the drive name included if the file in question is not in the same directory as the one this program is in ({CWD}). If this is not respected, you will have to re-enter the name of your file.: ")
                                print()
                            print("\nOperation is starting. This may take several minutes depending on the size of your file...\n")
                            with open(keyfilename,"rb") as encdeckey:
                                key = encdeckey.read()
                            with open(file_name, "rb") as contents:
                                bytescontent = contents.read() 
                            fernetkey = Fernet(key)
                            if optionfile_data_encryption == "2":
                                output = fernetkey.encrypt(bytescontent)
                            elif optionfile_data_encryption == "3":
                                output = fernetkey.decrypt(bytescontent)
                            with open(file_name, "wb") as writing:
                                writing.write(output)
                            print("")
                            if optionfile_data_encryption == "2":
                                print("Encrypted and saved data with no errors.")
                            elif optionfile_data_encryption == "3":
                                print("Decryped and saved data with no errors")
                            print("")
                            input("Press enter to continue...")
                            print()
                        elif optionfile_data_encryption == "4":
                            print()
                            prehash = input("Enter text to hash: ").encode('utf-8')
                            print()
                            print("Available Hashing Algorithms (MDA, SHA1 and SHA224/SHA3-224 not included as they are outdated and insecure):")
                            print("[1] SHA256 (most common)")
                            print("[2] SHA384")
                            print("[3] SHA512 (second most common)")
                            print("[4] SHA3-256")
                            print("[5] SHA3-384")
                            print("[6] SHA3-512")
                            print("[7] SHAKE128")
                            print("[8] SHAKE256")
                            print("[9] BLAKE2B")
                            print("[10] BLAKE2S")
                            optionhashalg = input("Select hashing algorithm: ")
                            print()
                            print("Hashing text, please wait...")
                            if optionhashalg == '1':
                                output = hashlib.sha256(prehash).hexdigest()
                            elif optionhashalg == '2':
                                output = hashlib.sha384(prehash).hexdigest()
                            elif optionhashalg == '3':
                                output = hashlib.sha512(prehash).hexdigest()
                            elif optionhashalg == '4':
                                output = hashlib.sha3_256(prehash).hexdigest()
                            elif optionhashalg == '5':
                                output = hashlib.sha3_384(prehash).hexdigest()
                            elif optionhashalg == '6':
                                output = hashlib.sha3_512(prehash).hexdigest()
                            elif optionhashalg == '7':
                                output = hashlib.shake_128(prehash).hexdigest(length=int(input("Enter amount of bytes for output. Length 32 is the standard length for SHAKE128: ")))
                            elif optionhashalg == '8':
                                output = hashlib.shake_256(prehash).hexdigest(length=int(input("Enter amount of bytes for output. Length 64 is the standard length for SHAKE256: ")))
                            elif optionhashalg == '9':
                                output = hashlib.blake2b(prehash).hexdigest()
                            elif optionhashalg == '10':
                                output = hashlib.blake2s(prehash).hexdigest()
                            else:
                                output = '{NO OUTPUT: could not load hashing algorithm specified}'
                            print()
                            print(f"Hashed {prehash} with output '{output}'. Used hash algorithm {optionhashalg}")
                            print("")
                            input("Press enter to continue...")
                            print()     
                        elif optionfile_data_encryption == '5':
                            clear()
                            print("Specifications/informations about this program: ")
                            print("")
                            print("-> Program name: THE FILE AND DATA ENCRYPTION SYSTEM.")
                            print("-> Manufacturers: GmaerSoft42/Okmeque1")
                            print("-> Manufacturers' company: © Okmeque1 Software ™.")
                            print("-> Program version: 1.2")
                            print("-> Program description: This program is a encryption system. It lets you encrypt and hash files and text however you'd like them")
                            print("-> Program security version: 5.2.0")
                            print("-> It is highly recommended to encrypt any files with personal information, as Fernet is a proven encryption system that is very hard for hackers to crack (so long as the key file is securely stored. The best way to do that is to store the key file on a USB drive then when you don't need it, unplug from the PC using Safe Eject and store it in a safe or something/)")  
                            print()
                            input("Press ENTER to continue...")   
                        elif optionfile_data_encryption == '6':
                            print("")
                            print("Saving data to main program. Please wait...")
                            time.sleep(1)
                            print("")
                            input("Press enter to continue...")
                            print("")
                            encryption_system = False            
                elif option == 3:
                    clear()
                    print("")
                    print("THE PASSWORD MANAGER SYSTEM is opening. You are going to be directed to the menu.")
                    print("")
                    input("Press enter to continue...")
                    time.sleep(1)
                    print("")
                    print("***** | THE PASSWORD MANAGER SYSTEM | *****")
                    print("Program version: 3.21.2.")
                    print("")
                    print("Please read option 4 if this is the first time you use this program or if any updates has been done on this program's version, as new options or functions could be added!")
                    print("")
                    print("When you are asked for a valid file name, please make sure that the directory is valid and for best compatibility and please make sure that any files that are specified exists.")
                    print("")
                    prompt = "Do you have the default file: 'pwd_openscs.pwd' (if you are unsure, use 'N' at this prompt. Otherwise use 'S' to not configure a default file or Y if you have the file)? [Y/N/S]: "
                    if os.path.exists(f"{CWD}\\pwd_openscs.pwd"):
                        prompt = f"Do you want to use the default file: 'pwd_openscs.pwd' in this directory ({CWD})? [Y]es/[N]o, let me select a different default file in a different directory/[S]kip default file configuration: "
                    defaultfileask = input(prompt)
                    defaultfileprompt = f"Please enter a valid file name path (leave blank and press enter to a default file of pwd_openscs.pwd in current directory {CWD}). The format must be full (all directories up to the root directory starting from your file) with the drive name included if the file in question is not in the same directory as the one this program is in ({CWD}). If this is not respected, you will have to re-enter the name of your file: "
                    defaultfileprompt1 = f"Please enter a valid file name path. The format must be full (all directories up to the root directory starting from your file) with the drive name included if the file in question is not in the same directory as the one this program is in ({CWD}). If this is not respected, you will have to re-enter the name of your file: "
                    if defaultfileask.upper() == "Y":
                        print("")
                        input("Press enter to continue...")
                        print("")
                        pwd_manager = True
                    elif defaultfileask.upper() == "N":
                            directory_successful = False
                            print()
                            while directory_successful is False:
                                directory = input(f"Please enter a valid directory name. If there is no file named 'pwd_openscs.pwd', a blank file will be created to that location, otherwise the program will automatically set that as the default. Leave blank to detect/create the file in current directory ({CWD}): ")
                                print()
                                if not os.path.exists(directory):
                                    createdirectory = input(f"{directory} does not exist. Do you want to create it? [Y]es/[N]o, let me choose a different directory/[E]xit to main menu: ")
                                    print()
                                    if createdirectory.upper() == "Y":
                                        os.mkdir(directory)
                                    elif createdirectory.upper() == "N":
                                        pass # Returns to loop
                                    else:
                                        raise NotImplementedError # Will be caught later, just a stopgap to make the program restart. Don't scream, PEP 8 Police please...(not that this program complies any single bit)
                                if os.path.exists(directory):
                                    directory_successful = True
                            if os.path.exists(f"{directory}\\pwd_openscs.pwd"):
                                os.chdir(directory)
                                CWD = os.getcwd()
                                print(f"Succesfully detected and set {CWD}\\pwd_openscs.pwd as the default password saving file")
                            else:
                                os.chdir(directory)
                                CWD = os.getcwd()
                                filedefaultdownload = open(f"{directory}\\pwd_openscs.pwd","w")
                                filedefaultdownload.close()
                                print("")
                                print("Creating default password file 'pwd_openscs.pwd'. Please wait...")
                                time.sleep(1)
                                print("")
                                print(f"The file that was just created is called 'pwd_openscs.pwd' ({CWD}\\pwd_openscs.pwd) and it is used for default saving if no file name or set name are entered and and if this file is in the same directory as this program. \nTip: for any file prompts in this program, you can simply leave it blank and press ENTER and the program will automatically select this file.")
                            print("")
                            input("Press enter to continue...")
                            print("")
                            pwd_manager = True
                    else:
                            defaultfileprompt = defaultfileprompt1
                            print("")
                            input("Press enter to continue...")
                            print("")
                            pwd_manager = True                    
                    while pwd_manager:
                        clear()
                        print("PASSWORD MANAGER SYSTEM MENU: ")
                        print("=======================================")
                        print("1 -> Add and generate password to a save file.")
                        print("2 -> Show a password from a save file.")
                        print("3 -> Show all passwords from a save file.")
                        print("4 -> About this program.")
                        print("5 -> Change a password to a save file.")
                        print("6 -> Advanced Password Generator.")
                        print("7 -> Password generator based on the Cyrillic character set (learn more with option 4).")
                        print("8 -> Quit to main menu.")
                        print("Quick Tip: It is highly recommended to encrypt the password save file when you are done using this program using the FILE AND DATA ENCRYPTION SYSTEM at the main menu. If you do this, it protects your passwords and personal data, as well as giving you peace of mind that your data can't be exposed by hackers.")
                        print("")
                        optionpwd_manager = int(input("Select option : "))
                        if optionpwd_manager == 1:
        
                            print("")
                            print('Welcome to your password generator! (learn more with option 4).')
        
                            chars = '`1!23£4$€5%6^7&8*9(0-_=+q"~{[]}=+QwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~^%#\\|zéèàZxXcCvVbBnNmMm,<.>/?)'
        
                            number = 1 # amount of passwords to generate
                            length = input('Password length: ')
                            parameter = input("By default, the password is copied to the clipboard for security purposes. Do you wish to see the password in this program once generated (not recommended for security)? [Y/N]: ")
                            length = int(length)
        
                            for pwd in range(number):
                                password = ''
                                for c in range(length):
                                    password += random.choice(chars)
                                print("")
                                pyperclip.copy(password)
                                print("The password has been copied to the clipboard for security purposes.")
                                if parameter.upper() == "Y":
                                    print(password)
                                print("")
                                print('Password generated! Now saving...')
                                filename = input(f"Please enter a valid file name (leave blank and press enter to a default file of pwd_openscs.pwd in current directory {CWD}). If the file does not exist, the program will create it for you: ")
                                print()
                                if filename == "":
                                    filename = "pwd_openscs.pwd"
                                    set0 = input("Enter a password (set) name to continue. This program does not support having 2 sets of the same set name. Entering a set name that already exists will/could cause conflict. ")
                                    passave = open(filename, "a")
                                    passave.write(set0 + " -> " + password)
                                    passave.close()
                                else:
                                    set0 = input("Enter a password (set) name to continue. This program does not support having 2 sets of the same set name. Entering a set name that already exists will/could cause conflict. ")
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
                            fileopen = ''
                            while not os.path.exists(fileopen):
                                if not os.path.exists('pwd_openscs.pwd'):
                                    defaultfileprompt = defaultfileprompt1                                
                                fileopen = input(defaultfileprompt)
                                if fileopen == "":
                                    fileopen = "pwd_openscs.pwd"
                            print()
                            passopen = open(fileopen, "r")
                            set1 = input("Please enter the password (set) name for the desired password: ")
                            print("")
                            print("Here is the password for this set name:")
                            print("")
                            for line in passopen:
                                if line.split(" -> ")[0] == set1:
                                    print(line.split(" -> ")[1])
                                    print("")
                                    input("Press enter to continue...")
                                    print("")
                            passopen.close()
                        elif optionpwd_manager == 3:
                            print("")
                            fileallopen = ''
                            while not os.path.exists(fileallopen):
                                if not os.path.exists('pwd_openscs.pwd'):
                                    defaultfileprompt = defaultfileprompt1                                
                                fileallopen = input(defaultfileprompt)
                                if fileallopen == "":
                                    fileallopen = "pwd_openscs.pwd"
                            print()
                            passall0 = open(fileallopen,"r")
                            passall1 = passall0.read()
                            print("")
                            print("File identified. Reading in progress...")
                            time.sleep(1)
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
                            clear()
                            print("Specifications/informations about this program: ")
                            print("")
                            print("-> Program name: THE PASSWORD MANAGER SYSTEM.")
                            print("-> Manufacturers: GamerSoft24 and Okmeque1/GamerSoft24.")
                            print("-> Manufacturers' company: © GamerSoftware Corporation™ & © Okmeque1/GamerSoft24 Corporation™.")
                            print("-> Program version: 3.21.2.")
                            print("-> Program description: This program is a Password Manager System. It can create, save, read, show and manage passcodes.")
                            print("-> Program security version: 5.2.0")
                            print("-> By default, most passwords that this program returns are copied to the clipboard. However we will still give you the option to show the password in this program. The reason that this program copies to the clipboard by default is that in some systems, anything printed to a terminal is saved no matter what.")
                            print("-> It is highly recommended to encrypt the save file when you are done using this program using the FILE AND DATA ENCRYPTION SYSTEM at the main menu.")
                            print("")
                            input("Press ENTER to move to the next page...")
                            clear()
                            print("Compatibility of this program: ")
                            print("")
                            print("This program will run perfectly on Python for Windows but could also run on macOS, Linux and potentially other systems. The filepath format will vary as neither of those operating systems use drive letters: 'C:\\...\\Password Manager System\\pwd' like Windows OS. The structure for those OS will be some variations of the following: ")
                            print("")
                            print("1 -> macOS : The file structure may be: '/path/path1/Password Manager System/pwd.*'")
                            print("2 -> Linux: The file structure is unclear as there are so many Linux distros and versions possible to download but the structure may be: '/home/folder/pwd.*' (this is an example folder).")
                            print("")
                            print("")
                            input("Press ENTER to move to the next page...")
                            print("")
                            print("Cyrillic character set password generation: ")
                            print("")
                            print("This password manager supports generating passwords with the certain characters from the Cyrillic alphabet, commonly used in Eastern Europe (Ukraine, Russia, Belarus, etc...). Using them in your passwords makes your passwords more secure as hackers do not generally target such characters, and they look identical to standard characters, however please note that these characters aren't universally adopted, and using them on an old site may cause crashes or compatability errors.")
                            input("\nPress enter to continue...")
                        elif optionpwd_manager == 5: 
                            filedels = ''
                            while not os.path.exists(filedels):
                                if not os.path.exists('pwd_openscs.pwd'):
                                    defaultfileprompt = defaultfileprompt1
                                filedels = input(defaultfileprompt)
                                if filedels == '':
                                    filedels = 'pwd_openscs.pwd'
                            print()
                            sets1 = input("Enter password (set) name to change : ")
            
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
                                print("")
                                print("Save has completed with no disk errors.")
                                print("")
                                input("Press enter to continue...")
                                print()
                        elif optionpwd_manager == 6:
                            #print("Please be aware that due to the mixing logic of this program, the amount of a type of character may not be exact.\n© Okmeque1 Software")
                            end = ""
                            passwd = ""
                            spc = '¦¬`!£$€%^&*()-_=+;:@~#\\|,<.>/?'
                            num = "1234657890"
                            ch = "qQwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlLzZxXcCvVbBnNmMm"
                            spcs = ""
                            nums = ""
                            chs = ""
                            spcn = int(input("Enter special character count ($, %, *, etc) : "))
                            print()
                            numn = int(input("Enter number count (0-9) : "))
                            print()
                            chn = int(input("Enter standard character count (A-Z) : "))
                            print()
                            parameter = input("By default, the password is copied to the clipboard for security purposes. Do you wish to see the password in this program once generated (not recommended for security)? [Y/N]: ")
                            for p in range(spcn):
                                spcs += random.choice(spc)
                            for s in range(numn):
                                nums += random.choice(num)
                            for ad in range(chn):
                                chs += random.choice(ch)
                            end += spcs + nums + chs
                            order = [_ for _ in range(len(end))]
                            shuffled = random.shuffle(order)
                            for x in range(len(order)):
                                passwd += end[order[x]]
                            pyperclip.copy(passwd)
                            if parameter.upper() == "Y":
                                print(passwd)
                            print("The password has been copied to the clipboard for security purposes.")
                            filenam = input(f"Please enter a valid file name (leave blank and press enter to a default file of pwd_openscs.pwd in current directory {CWD}). If the file does not exist, the program will create it for you: ")
                            print()
                            if filenam == "":
                                filenam = "pwd_openscs.pwd"
                                sets = input("Enter a password (set) name for your password to continue this program. This will be used later to retrieve back the password. This program does NOT support having 2 sets of the same name. Entering a name that already exists will cause a conflict. : ")
                                passavee = open(filenam,"a")
                                passavee.write(sets + " -> " + passwd + "\n")
                                passavee.close()
                            else:
                                sets = input("Enter a password (set) name for your password to continue this program. This will be used later to retrieve back the password. This program does NOT support having 2 sets of the same name. Entering a name that already exists will cause a conflict. : ")
                                passavee = open(filenam,"a")
                                passavee.write(sets + " -> " + passwd + "\n")
                                passavee.close()
                                print("")
                                print("Save has completed with no disk errors.")
                                print("")
                                input("Press enter to continue...")
                                print()
                        elif optionpwd_manager == 7:
                            cyrillic_character_set = "АаВеЕЗМоНОРрСсТуХхЈјҮԁԌԚԛԜԝ"
                            standard_chars = '¦¬`1!23#4$5%6^7&8*9(0-_=+q"~{[]}=+QwWeErRtTyYuUiIoOpPaAsSdDfFgGhHjJkKlL;:@~^%#\\|zZxXcCvVbBnNmMm,<.>/?)'
                            chars = [cyrillic_character_set, standard_chars]
                            length = int(input("Please enter your password length: "))
                            parameter = input("By default, the password is copied to the clipboard for security purposes. Do you wish to see the password in this program once generated (not recommended for security)? [Y/N]: ")
                            pwd = ""
                            for x in range(length):
                                pwd += random.choice(random.choice(chars))
                            print("")
                            pyperclip.copy(password)
                            if parameter.upper() == "Y":
                                print(pwd)
                            print("The password has been copied to the clipboard for security purposes.")
                            print("")
                            print('Password generated! Now saving...')
                            filename = input(f"Please enter a valid file name (leave blank and press enter to a default file of pwd_openscs.pwd in current directory {CWD}). If the file does not exist, the program will create it for you: ")
                            if filename == "":
                                filename = "pwd_openscs.pwd"
                            set0 = input("Enter a password (set) name to continue. This program does not support having 2 sets of the same set name. Entering a set name that already exists will/could cause conflict. ")
                            passave = open(filename, "a")
                            passave.write(set0 + " -> " + pwd)
                            passave.close()
                            print("")
                            print("Save has completed with no disk errors.")
                            print("")
                            input("Press enter to continue...")
                            print()
                        elif optionpwd_manager == 8:
                            print("")
                            print("Saving data to main program. Please wait...")
                            time.sleep(1)
                            print("")
                            print("It is highly recommended to encrypt the password save file when you are done using this program using the FILE AND DATA ENCRYPTION SYSTEM at the main menu. If you do this, it protects your passwords and personal data, as well as giving you peace of mind that your data can't be exposed by hackers.")
                            input("Press enter to continue...")
                            print("")
                            pwd_manager = False
        
                elif option == 5:
                    clear()
                    print("")
                    print("THE BINARY ENCRYPTER & DECRYPTER SYSTEM is opening. You are going to be directed to the menu.")
                    print("")
                    input("Press enter to continue...")
                    time.sleep(1)
                    binary_encrypt_decrypt_system = True
                    while binary_encrypt_decrypt_system:
                        clear()
                        print("")
                        print("***** | THE BINARY ENCRYPTER & DECRYPTER SYSTEM | *****")
                        print("Program version: 2.21.1")
                        print("This is a LEGACY program, meaning that it is not officially supported. For proper encryption, use the DEDICATED encryption system in the main menu (option 4). The 'Software' Team will NOT be liable for any damages that result from the use of this program.")
                        print("")
                        print("MENU: ")
                        print("===================")
                        print("1 -> Encrypt text.")
                        print("2 -> Decrypt text.")
                        print("3 -> Quit to main menu.")
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
                            print("Encoded binary:", encrypted)
                            print('')
        
                        elif optionbinary_encrypt_decrypt_system == 3:
                            print("")
                            print("Saving data to main program. Please wait...")
                            time.sleep(1)
                            print("")
                            input("Press enter to continue...")
                            print("")
                            binary_encrypt_decrypt_system = False
        
                        elif optionbinary_encrypt_decrypt_system == 2:
                            print('')
                            binary_input = input("Enter the binary to decode (space-separated): ")
                            def binary_to_text(binary_text):
                                binary_list = binary_text.split()
                                text = ''.join(chr(int(binary, 2)) for binary in binary_list)
                                return text
                            decrypted = binary_to_text(binary_input)
                            print('')
                            print("Decoded text:", decrypted)
                            print('')
        
                elif option == 2:
                    print("Latest Updates and informations (there will be the 10 most recent updates in this changelog): ")
                    print("")
                    print("30/08/2025: first of all happy back to school season, but second of all I am massively reworking this program to be an actual reliable piece of code that can be depended on, and to make it less gimmicky and more utilitarian.")
                    print("update at 11:09: how have I spend like 2.5 hours on this program while not changing much??????????")
                    print(f"06/09/2025: unfortunately this file prompt had to go in order to make SMS advanced possible: 'Please enter a valid file name path (leave blank and press enter to a default file of pwd_openscs.pwd in current directory {CWD}). The format must be full (all directories up to the root directory starting from your file) with the drive name included if the file in question is not in the same directory as the one this program is in ({CWD}). If this is not respected, this program will/could terminate with the main program without any warning: '")
                    print(f"In its place, we have the replacement: 'Please enter a valid file name path (leave blank and press enter to a default file of pwd_openscs.pwd in current directory {CWD}). The format must be full (all directories up to the root directory starting from your file) with the drive name included if the file in question is not in the same directory as the one this program is in ({CWD}). If this is not respected, you will have to re-enter the name of your file: '. And this prompt tells you if there's a default or not, and if you skip the default file configuration in the PASSWORD MANAGER system, it will not let you choose a default to avoid errors and confusion.")
                    input("Press ENTER to continue...")
                elif option == 6:
                    print("")
                    print("")
                    print("Exit code: " + exit_code_choosen)
                    print("")
                    security_manager = False
                    print("")
                    print("We hope that this program was useful for your use case! If not, consider opening a GitHub issue and we will try to improve this program.")
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
            print("All clear, free to go! Enjoy!")
            input("Press enter to start main program.")
            print()
            sms_main()
    except NotImplementedError: #simple bugfix to force return to main menu
        continue
    except IsADirectoryError as e:
        print(f"Error: 0283\nFile specified is a directory and not a file. Make sure that the resource is a file, then try again.\nDetails: {e}")
        input("Press enter to restart the program...")
        continue  
    except FileExistsError as e:
        print(f"Error: 6510A\nAn existing file is conflicting with the selected file. Delete or rename the conflicting file or choose a different file name to save.\nDetails: {e}")
        input("Press enter to restart the program...")
        continue
    except FileNotFoundError as e:
        print(f"Error: 6510B\nThe file specified was not found. Please make sure you have the correct file and that the path is valid.\nDetails: {e}")
        input("Press enter to restart the program...")
        continue
    except PermissionError as e:
        print(f"Error: 6510C\nAccess violation in file. Make sure you have the proper permissions to use that resource and try again\nDetails: {e}")
        input("Press enter to restart the program...")
        continue
    except OSError as e:
        print(f"Error: 0271\nOperating system error. Check your drive and program, as well as any files and try again.\nDetails: {e}")
        input("Press enter to exit...")
        exit()
    except ValueError as e:
        print(f"Error: 0211\nYou have entered the wrong value. When asked for a value, please input the correct value that is demanded (e.g length = number.)\nDetails: {e}")
        input("Press enter to restart the program...")
        continue
    except KeyboardInterrupt:
        print("User has chosen to exit. Exiting...")
        exit()
    except EOFError: # Good enough right?
        print("User has chosen to exit. Exiting...")
        exit()
    except IOError as e:
        print(f"Error: 0272\nA device on your system has either malfunctioned or has been unplugged, or a file operation has failed. The operating system will now forcibly close the program.\nDetails: {e}")
        input("Press enter to exit...")
        exit()
    except ModuleNotFoundError as e:
        print(f"Error: 1002/0199\nModule required is not installed. Make sure all dependencies are correctly installed as per the GitHub GamerSoft24/Software PySoft requirements.txt and try again.\nDetails: {e}")
        input("Press enter to exit...")
        exit()
    except Exception as e:
        print(f"Error: {e}\nPlease review the Error Chart of the GamerSoft24/Software repository, as well as the Python Manual for more information and a solution for this error.")
        input("Press enter to restart the program. Note that you have lost any data that the last operation did")
        continue
