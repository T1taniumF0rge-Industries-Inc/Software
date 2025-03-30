import sqlite3
import pwdmgr
import pwdgen
import encryption
import os
key = False
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def main():
    pwdmanager = pwdmgr.PasswordManager()
    while True:
        clear()
        print("*****|DATABASE PASSWORD MANAGER|*****")
        print("[1] Generate password to database")
        print("[2] Add custom password to database")
        print("[3] Advanced password generator")
        print("[4] Update password")
        print("[5] Delete password")
        print("[6] Delete database")
        print("[7] Not in use")
        print("[8] View all passwords")
        print("[9] Generate encryption key")
        print("[10] Encrypt database")
        print("[11] Decrypt database")
        print("[12] Refresh Database - This operation must be performed if the database has been deleted")
        print("[13] Quit")
        option = int(input("Please select an option: "))
        if option == 1 or option == 2 or option == 3:
            if option == 1:
                length = int(input("Please enter the length of your password: "))
                pwd = pwdgen.generate_pwd(length)
                print(f"Your password is: {pwd}")
            if option == 2:
                pwd = input("Please enter your desired password: ")
            if option == 3:
                print("Please note that this option may not give the exact number of characters that are inputted due to the way the mixing logic functions.")
                special_char = int(input("Please enter the amount of special characters you want in your password: "))
                number_char = int(input("Please enter the number of number characters in you want in your password: "))
                std_char = int(input("Enter the amount of standard characters you want in your password: "))
                pwd = pwdgen.adv_pwd(special_char,number_char,std_char)
                print(f"Your password is: {pwd}")
            name = input("Enter a name for your password: ")
            username = input("Enter the username for the desired application: ")
            site = input("Enter the name of the site (if applicable): ")
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
            confirmation = input("This action is irrevocable, and you will not be able to retrieve this password after the deletion. Proceed? [Y/N]: ")
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
            confirmation = input("This action is irrevocable, and you will not be able to retrieve this password after the deletion. Proceed? [Y/N]: ")
            if confirmation == "Y":
                confirm = input("To proceed, type 'True': ")
                if confirm == "True":
                    pwdmanager.del_all()
                    input("Deleted password successfully. Press ENTER to continue...")
                else:
                    input("Operation cancelled. Press ENTER to continue...")
            else:
                input("Operation cancelled. Press ENTER to continue...")  
        if option == 7:
                print("An error has occurred. To continue,")
                print(" → Press enter to return to the main menu")
                print(" → Press CTRL + C to terminate this program. You will lose any unsaved data in any open programs.")
                print("Press any ENTER to continue. Error : 0FA3E22")
                input("")          
                print("Bad Value for memory address 70 72 69 6E 74 28 22 42 61 64 20 56 61 6C 75 65 20 66 6F 72 20 6D 65 6D 6F 72 79 20 61 64 64 72 65 73 73 20 20 5C 6E 22 29 \n The following operation has been terminated.")
                input("You may choose to continue by pressing ENTER. The program will ignore the error and attempt to continue. If you press CTRL + C, the program will terminate immediately. You will lose any unsaved work in any open programs.")
        if option == 8:
            rows = pwdmanager.fetch()
            for x in rows:
                print(x)   
            input("Press ENTER to continue...")
        if option == 9:
            filename = input("Please enter a valid file name to store your encryption key. For maximum compatability, it is recommended to use the *.frn file extension: ")
            encryption.keygen(filename)
            input("Key successfully saved. Press ENTER to continue...")
        if option == 10 or option == 11:
            keyname = input("Please enter a valid fernet key file name. The format must be A:\directory\keyfile.frn: ")
            dbname = input("Please enter a valid file name (The Database is usually stored in the same directory as this python file). The format must be A:\directory\pwdfile.extension: ")
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
def test(): 
    pwdmanager = pwdmgr.PasswordManager()
    pwdmanager.add_pwd("gmail","okmeque1.corporation@gmail.com","https://mail.google.com","very good password.",0,"")
    for x in pwdmanager.fetch():
        print(x)
    print(pwdmanager.select("1"))
    pwdmanager.update_pwd("1","gmail","okmeque1.corporation@gmail.com","https://github.com/GmaerSoft","horrible password") #gmaersoft42, go explore it while i TEST MY FUNCTION
    print(pwdmanager.select("1"))
    pwdmanager.del_pwd("1")
    for x in pwdmanager.fetch():
        print(x)
if __name__ == "__main__":
    def start():
        try:
            main()
        except ValueError:
            print("STOP : 0211\nYou have entered the wrong values for an input. When asked for a value, make sure that it is the CORRECT value.")
            input("Press ENTER to RESTART program...")
            start()
        except sqlite3.DatabaseError as e:
            input(f"STOP : Database Error - {e}\nTo continue, you must DECRYPT the database file.\n→ Press ENTER to decrypt the file...\n→ Press CTRL + C to terminate the program. You will lose any unsaved data in any open programs.")
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
            input(f"STOP : {e}\nReview the error chart and Python manual for more info.\nPress ENTER to return to main menu...")
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
            input(f"STOP : {e}\nReview the error chart and Python manual for more info.\nPress ENTER to return to main menu...")
            start()