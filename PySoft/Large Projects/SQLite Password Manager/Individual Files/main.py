import sqlite3
import pwdmgr
import pwdgen
import encryption
import os
import pyperclip
key = False
CWD = os.getcwd()
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def main():
    pwdmanager = pwdmgr.PasswordManager()
    while True:
        clear()
        print("*** DATABASE PASSWORD MANAGER ***")
        print("[1] Generate password to database")
        print("[2] Add custom password to database")
        print("[3] Advanced password generator")
        print("[4] Update Password")
        print("[5] Delete password")
        print("[6] Delete database")
        print("[7] Cyrillic Password Generation")
        print("[8] View all passwords")
        print("[9] Generate Encryption key")
        print("[10] Encrypt database")
        print("[11] Decrypt database")
        print("[12] Refresh Database - This operation must be performed if the database has been deleted to restore the original format")
        print("[13] Quit")
        option = int(input("Please select an option: "))
        if option in (1,2,3,7):
            if option == 1:
                length = int(input("Please enter the length of your password: "))
                pwd = pwdgen.generate_pwd(length)
            if option == 2:
                pwd = input("Please enter your desired password: ")
            if option == 3:
                print("Please note that this option may not give the exact number of characters that are inputted due to the way the mixing logic functions.")
                special_char = int(input("Please enter the amount of special characters you want in your password: "))
                number_char = int(input("Please enter the number of number characters in you want in your password: "))
                std_char = int(input("Enter the amount of standard characters you want in your password: "))
                pwd = pwdgen.adv_pwd(special_char,number_char,std_char)
            if option == 7:
                 print("Please note that these characters cannot be typed using a standard ANSI keyboard and need to be copy pasted from this program. Also note that since Cyrillic characters aren't widely used outside of Eastern Europe (Ukraine, Russia, Belarus, etc...), it may break older websites or throw errors about compatability errors.")
                 pwd_length = int(input("Please enter the length of your desired password: "))
                 pwd = pwdgen.cyrillic_pwd(pwd_length)
            pyperclip.copy(pwd)
            print(f"The password has been copied to clipboard. Use CTRL-V to paste it.")
            name = input("Enter a name for your password: ")
            username = input("Enter the username for the desired application: ")
            site = input("Enter the name of the site or application (if applicable): ")
            pwdmanager.add_pwd(name, username, site, pwd)
            input("Saved password successfully. Press ENTER to continue...")
        if option == 4:
            rows = pwdmanager.fetch()
            for x in rows:
                print(x)
            id = input("Please enter the ID of your password. It is the number at the very left of the window: ")
            name = input("Enter a new name for your password: ")
            username = input("Enter the new username for the desired application: ")
            site = input("Enter the new name of the site (if applicable): ")
            pwd = input("Enter a new password: ")
            pwdmanager.update_pwd(id, name, username, site, pwd)
            input("Updated password successfully. Press ENTER to continue...")
        if option == 5:
            rows = pwdmanager.fetch()
            for x in rows:
                print(x)
            id = input("Please enter the ID of your password. It is the number at the very left of the window: ")                                 
            confirmation = input("This action is irrevokable, and you will not be able to retrieve this password after the deletion. Proceed? [Y/N]: ")
            if confirmation == "Y":
                confirm = input("To proceed, type 'True': ")
                if confirm == "True":
                    pwdmanager.del_pwd(id)
                    input("Deleted password successfully. Press ENTER to continue...")
                else:
                    input("Operation cancelled. Press ENTER to continue...")
            else:
                input("Operation cancelled. Press ENTER to continue...")
        if option == 6:
            confirmation = input("This action is irrevokable, and you will not be able to retrieve any passwords in the database file after the deletion. Proceed? [Y/N]: ")
            if confirmation == "Y":
                confirm = input("To proceed, type 'True': ")
                if confirm == "True":
                    pwdmanager.del_all()
                    input("Deleted password successfully. Press ENTER to continue...")
                else:
                    input("Operation cancelled. Press ENTER to continue...")
            else:
                input("Operation cancelled. Press ENTER to continue...")  
        if option == 8:
            rows = pwdmanager.fetch()
            for x in rows:
                print(x)   
            input("Press ENTER to continue...")
        if option == 9:
            filename = input("Please enter a valid file name to store your encrytion key. For maximum compatability, it is recommended to use the *.frn file extension: ")
            encryption.keygen(filename)
            input("Key successfully saved. Press ENTER to continue...")
        if option == 10 or option == 11:
            keyname = input("Please enter a valid fernet key file name. The format must be a:\directory\keyfile.frn: ")
            dbname = input(f"Please enter a valid file name (The Database is usually stored in the same directory as this python file and is named 'pwd.db'. Leave blank and press enter to use default of 'pwd.db' in {CWD} (current directory)).: ")
            if dbname == '':
                 dbname = f'{CWD}\\pwd.db'
            if option == 10:
                print("Encrypting file. This may take several minutes...")
                encryption.enc(keyname, dbname)
                input("File successfully encrypted. Press ENTER to continue...")
            if option == 11:
                print("Decrypting file. This may take several minutes...")
                encryption.dec(keyname, dbname)
                input("File successfully decrypted. Press ENTER to continue...")
        if option == 12:
            start()
        if option == 13:
            exit()
if __name__ == "__main__":
    def start():
        try:
            main()
        except ValueError:
            print("STOP : 0211\nYou have entered the wrong values for an input. When asked for a value, make sure that it is the CORRECT value.")
            input("Press ENTER to RESTART program...")
            start()
        except sqlite3.DatabaseError as e:
            os.chdir(CWD)
            if not os.path.exists("pwd.db"):
                        filedefaultdownload = open("pwd.db","w")
                        filedefaultdownload.close()
                        input(f"Created database file in {CWD}. Press ENTER to continue...")
                        start()
            input(f"STOP : Database Error - {e}\nTo continue, you may have DECRYPT the database file.\n→ Press ENTER to decrypt the file...\n→ Press CTRL + C to terminate the program. \nIf problems persist, make sure that you have the appropriate permissions to use the file and that your disks are not corrupted.")
            keyfile = input("Please enter a valid fernet key file. The format must be A:\directory\subdirectory\keyfile.frn: ")
            file = input("Please enter a valid encrypted file to decrypt: ")
            try:
                encryption.dec(keyfile,file)
                start()
            except Exception as e:
                input(f"STOP : {e}\nPress ENTER to retry decryption...")
                start()
        except KeyboardInterrupt:
            print("STOP : 0270\nUser has chosen to exit. Exiting...")
            exit()
        except SystemExit:
            print("Exiting...")
            exit()
        except Exception as e:
            input(f"STOP : {e}\nReview the GitHub GamerSoft24/Software PySoft error chart and Python manual for more info.\nPress ENTER to return to main menu...")
            start()
try:
    start()
except KeyboardInterrupt:
            print("STOP : 0270\nUser has chosen to exit. Exiting...")
            exit()
except SystemExit:
            print("Exiting...")
            exit()
except Exception as e:
            input(f"STOP : {e}\nReview the GitHub GamerSoft24/Software PySoft the error chart and Python manual for more info.\nPress ENTER to return to main menu...")
            start()
