import os
import time
from tkinter import messagebox as msgbox
import tkinter as tk
def fm(sdir):
    try:
        try:
            dshow = "dir " + sdir + " /p"
            os.system(dshow)
            valid = [1,2,3,4,5,6,7,8,9,10,11]
            print("Operations :")
            print("[1] Change DIR")
            print("[2] Run file ")
            print("[3] Make FOLDER")
            print("[4] Make FILE")
            print("[5] Move FILES")
            print("[6] Copy FILES")
            print("[7] None")
            print("[8] Enter CMD.EXE")
            print("[9] Delete DIR")
            print("[10] Delete FILE")
            print("[11] Exit")
            print("Current DIR : " + sdir)
            userchoice = int(input("Choose : "))
            print("Loading specified utility,please wait...")
            badchoice = True
            for x in range(len(valid)):
                if valid[x] == userchoice:
                    badchoice = False
                    break
            if badchoice == True:
                input("Invalid choice.Press ENTER to continue")
                fm(sdir)
            if userchoice == 1:
                chdir = input("Enter a VALID directory to change to : ")
                sdir = chdir
                input("DIR changed.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 2:
                runfl = input("Enter a VALID file to run :")
                os.system(runfl)
                input("No Errors were logged.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 3:
                mkdir = input("Enter DIR file path/name(Example : C:\ST\TEST) : ")
                mkdir0 = "mkdir " + mkdir
                os.system(mkdir0)
                input("DIR made with no errors.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 4:
                make = input("Enter a VALID file name to create(Example : C:\ST\TEST\TEST.TXT) : ")
                with open(make,"x"):
                    input("File made with no errors.Press ENTER to continue...")
                    fm(sdir)
            elif userchoice == 5:
                move = input("From : ")
                to = input("To : ")
                moveto = "move " + move + " " + to
                os.system(moveto)
                input("Moved " + move + " to " + to + " with no errors.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 6:
                copy = input("From : ")
                dest = input("To : ")
                copyto = "copy " + copy + " " + dest
                os.system(copyto)
                input("Copied " + copy + " to " + dest + " with no errors.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 7:
                print("Loading specified utility, please wait...")
                time.sleep(3)
                print("FAILED : Exiting...")
                time.sleep(1)
                return
            elif userchoice == 8:
                os.system("C:\Windows\System32\CMD.EXE")
            elif userchoice == 9:
                rmdir = input("Enter DIR to remove : ")
                os.remove(rmdir)
                input("Removed DIR with no errors.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 10:
                rmf = input("Enter FILE to remove : ")
                os.remove(rmf)
                input("Removed File with no errors.Press ENTER to continue...")
                fm(sdir)
            elif userchoice == 11:
                return
        except PermissionError:
            print("STOP : 0210\nYou do not have the permissions to edit this file.Exiting...")
            return
        except FileNotFoundError:
            sev = tk.Tk()
            sev.withdraw()
            severe = msgbox.showerror("Severe","6510B:\nYou must specify a valid file/folder.")
            fm(sdir)
        except EOFError:
            print("STOP : 0250\nYou have raised EOFError and will now exit.Details : User raised EOFError unexpectedly which was caught by an except block.")
            return
        except ValueError:
            input("STOP : 0211\nInvalid parameter.Acceptable values are from 1-9.Press ENTER to continue...")
            fm(sdir)
        except KeyboardInterrupt:
            print("STOP : 0270\nKeyboardInterrupt called.Now exiting...")
            return
        except IOError:
            print("STOP : 6510C\nAn I/O error has occured.Exiting...")
            return
        except:
            input("STOP : 770A\nAn unexpected error occured.Press ENTER to continue...")
            fm(sdir)
    except:
        recover = input("STOP : 0261\nFM has caused an error.Press ENTER to attempt to recover[any invalid option to abort.]")
        if recover == '':
            fm(sdir)
print("WARNING!This is an UNSTABLE release.Crashes are to be EXPECTED and this program is best suited to PROFESSIONAL users.To avoid CRASHES,please only use valid file names.")
fm(input("Starting DIR : "))
