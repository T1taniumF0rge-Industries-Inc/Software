import os
import pyperclip
def rnp(amount, namestr): #un petit flippity
    basestr = "https://flippity.net/rp.php?c=" #the base string to actually bring you to the wheel URL
    things = "" #things that are in the wheel
    wheelname = f"&t={namestr}" #you want your wheel to have personality right?
    for x in range(int(amount)):
        things += f"{x},"
    things.strip(",")
    final_link = basestr + things + wheelname #link generation, please wait
    pyperclip.copy(final_link)
    return final_link
if __name__ == "__main__":
    def start():
        try:
            a = input("Select the number of elements: ")
            b = input("Input the name of your wheel: ")
            d = rnp(a,b)
            if int(a) > 1855:
                print("WARNING! Flippity is known to refuse requests to their random pickers if the amount of elements exceeds 1855. ")
                confirmation = input("Proceed with operation? [Y/N]: ")
                if confirmation != "Y" or confirmation != "y":
                    print("Operation cancelled. Program is now restarting...")
                    start()
            if d != 0:
                print(d)
            print("For added convenience, the link has been pasted into the clipboard")
            input("Press ENTER to EXIT...")
        except ValueError as e:
            print("You have entered the wrong value type for what was asked. If you were asked for a number, enter a number.")
            print(f"Details: {e}")
            input("Press ENTER to RESTART the program...")
            start()
        except KeyboardInterrupt:
            print("User has chosen to exit. Exiting...")
        except Exception as e:
            print(f"ERROR: {e}\nReview the error chart and the Python Manual for more info.")
            input("Press ENTER to RESTART the program...")
            start()
    start()
