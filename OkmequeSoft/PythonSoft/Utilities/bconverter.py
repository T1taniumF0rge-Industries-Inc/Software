def start():
    print("BINARY CONVERTER \n Program version 1.0.0 \n Creator = Okmeque1")
    print("Please choose one of the following...")
    print("INFO : This program does not support HEXADECIMAL (AA00) and ONLY functions with class INT.")
    print(" 1 → Convert INT → BINARY")
    print(" 2 → Convert BINARY → INT")
    chose = input("Enter '1' or '2' . Any invalid option will quit the program. → ")
    if chose == "1":
        int_convert()
    if chose == "2":
        bconvert()
def int_convert():
    try:
        save = []
        rest = 0
        toconvert = input("Enter your number to convert → ")
        base = input("Enter BASE set(a default of BASE2 is set and is recommended for most usage cases.) → ")
        if base == "":
            base = 2
        base = int(base)
        toconvert = int(toconvert)
        temp = toconvert
        while temp >= 1:
            rest = temp % base
            temp //= base
            save.append(str(rest))
        print("Your BINARY STRING is " + "".join(save[::-1]) + " with BASE" + str(base) + ".")
    except ValueError:
        print("STOP : 0211 \nCode is either invalid or bad value was specified")
        input("Press ENTER to exit...")
        return None
    except EOFError or KeyboardInterrupt:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        return None
def bconvert():
    try:
        returnint = 0
        base2 = 1
        bintoconvert = input("Enter binary STRING into prompt. → ")
        base = input("Enter a BASE set(a default of BASE2 is recommended for most usage cases.) → ")
        if base == "":
            base = 2
        base = int(base)
        for x in bintoconvert[::-1]:
            returnint += int(x) * base2
            base2 *= base
        print("The decoded number of " + bintoconvert + " BINARY STRING is " + str(returnint) + " with BASE" + str(base) + ".")
    except ValueError:
        print("STOP : 0211 \nCode is either invalid or bad value was specified")
        input("Press ENTER to exit...")
        return None
    except EOFError or KeyboardInterrupt:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        return None        
start()
