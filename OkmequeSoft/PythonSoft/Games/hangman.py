import random
try:
    B = 1
    wrong = True
    print("HANG-MAN - Okmeque1 edition")
    file = input("Please enter a valid file name (none to default of G:\python\demo\words.txt). The format must be a:\directory\wordfile.txt : ")
    if file == "":
        file = "G:\python\demo\words.txt"
    fileopen = open(file,"r")
    ninety = []
    w = ["WRONG","No, just no","Swing and a miss!","Error, error. Bad answers.","Failure","May I suggest thinking?","Try harder please.","How about no?"]
    hf = [  [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" "," "," "," "," "," "],
            [" ","|"," "," "," "," "],
            [" ","|"," "," "," "," "],
            [" ","|"," "," "," "," "],
            [" ","|"," "," "," "," "]   ]
    for line in fileopen:
        ninety.append(line.strip())
    RC = random.choice(ninety)
    c = [""]
    c = c * (len(RC))
    d = 0
    while B == 1:
        print(c)
        wrong = True
            
        A = input("Enter letter." + str(len(RC)) + " is the length of this word : ")
        
        for i in range(len(RC)):
            if A == RC[i]:
                print("Correct at ",i)
                wrong = False
                c[i] = A 

        if "".join(c) == RC:
            print("Game won!")
            print("The word was : " + RC)
            B = 2

        if wrong == True:
            print(random.choice(w))
            if d == 0:
                hf[0][1] = "|"
                hf[1][1] = "|"
                hf[2][1] = "|"
                hf[3][1] = "|"
            elif d == 1:
                hf[0][2] = "-"
                hf[0][3] = "-"
                hf[0][4] = "|"
            elif d == 2:
                hf[1][3] = "-"
                hf[1][4] = "-"
                hf[1][5] = "-"
                hf[2][3] = "|"
                hf[2][4] = " "
                hf[2][5] = "|"
                hf[3][3] = "-"
                hf[3][4] = "-"
                hf[3][5] = "-"
            elif d == 3:
                hf[4][4] = "|"
                hf[5][4] = "|"
                hf[6][4] = "|"
            elif d == 4:
                hf[5][3] = "-"
            elif d == 5:
                hf[5][5] = "-"
            elif d == 6:
                hf[7][3] = "/"
            elif d == 7:
                hf[7][5] = "\ "
            for x in range(8):
                print("".join(hf[x]))
            d = d + 1
            print("Failed : " + str(d))
        if d == 7:
            print("WARNING!You are at 7 failed attempts.At 8 failed attempts the computer will terminate this program!.")
        elif d == 8:
            print("You lost! The word was " + RC)
            B = 2
except FileNotFoundError:
    print("STOP : 6510B\nThe specified file does not exist.Make sure that the file exists and try again.")
    input("Press ENTER to exit...")
    exit()
except EOFError or KeyboardInterrupt:
    print("STOP : 0250/0270\nThe user has chosen to exit.Exiting...")
