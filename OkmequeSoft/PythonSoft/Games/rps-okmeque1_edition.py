import random
import time
def u1(cpts,pts,rnd,psel):
    if rnd == 1 or rnd == 2 or rnd == 5:
        input("Nothing happened.Press ENTER to continue")
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 3 or rnd == 6:
        print("Player 1 has won a point!")
        pts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 4:
        print("Computer 1 has won a point!")
        cpts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
def u2(cpts,pts,rnd,psel):
    if rnd == 1 or rnd == 5 or rnd == 2:
        input("Nothing happened.Press ENTER to continue")
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 3 or rnd == 6:
        print("Computer 1 has won a point!")
        cpts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 4:
        print("Player 1 has won a point!")
        pts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
def u3(cpts,pts,rnd,psel):
    if rnd == 1 or rnd == 6 or rnd == 5:
        print("Computer 1 has won a point!")
        cpts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts)
    elif rnd == 3 or rnd == 4:
        input("Nothing happened.Press ENTER to continue")
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts)
    elif rnd == 2:
        print("Player 1 has won a point!")
        pts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
def u4(cpts,pts,rnd,psel):
    if rnd == 3 or rnd == 4 or rnd == 5 or rnd == 6:
        input("Nothing happened.Press ENTER to continue")
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 1:
        print("Player 1 has won a point!")
        pts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 2:
        print("Computer 1 has won a point!")
        cpts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
def u5(cpts,pts,rnd,psel):
    if rnd == 2 or rnd == 4 or rnd == 5:
        input("Nothing happened.Press ENTER to continue")
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 3 or rnd == 1:
        print("Player 1 has won a point!")
        pts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 6:
        print("Computer 1 has won a point!")
        cpts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
def u6(cpts,pts,rnd,psel):
    if rnd == 3 or rnd == 4 or rnd == 6:
        input("Nothing happened.Pres ENTER to continue")
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 1:
        print("Computer 1 has won a point!")
        cpts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
    elif rnd == 2 or rnd == 5:
        print("Player 1 has won a point!")
        pts += 1
        if rps(cpts,pts,psel) == True:
            rps_psel1(cpts,pts,psel)
        rps(cpts,pts,psel)
def storage():
    return 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv'
def whowin(cpts,pts,psel):
    if psel == 2:
        if pts >= cpts:
            print("Player has won!")
            print("Player 1 points : " + str(cpts))
            exit()
        else:
            print("Player 1 has won!")
            print("Player points : " + str(pts))
            exit()
    elif pts >= cpts:
        print("Player 1 has won!")
        print("Computer points : " + str(cpts))
        exit()
    elif pts == 310 and cpts == 310:
        return 'Ended'
    else:
        print("Computer 1 has won!")
        print("Player 1 points : " + str(pts))
        exit()
def rps(cpts,pts,psel):
    if cpts == 10 or pts == 10:
        whowin(cpts,pts,psel)
    elif psel == 2:
        return True
    print("Computer points : " + str(cpts))
    print("Player points : " + str(pts))
    rn = [1,2,3,4,5,6]
    rf = random.choice(rn)
    print("Type string 'Exit' to exit the game.")
    uchoice = input("Enter 1,2,3,4,5,6 = ")
    print("Rock...",end='\r')
    time.sleep(0.5)
    print("Rock...Paper...",end='\r')
    time.sleep(0.5)
    print("Rock...Paper...Scissors...",end='\r')
    time.sleep(0.5)
    print("Rock...Paper...Scissors...SHOOT!")
    if uchoice == "1":
        print("Computer 1 has chosen move " + str(rf))
        u1(cpts,pts,rf,psel)
    elif uchoice == "2":
        print("Computer 1 has chosen move " + str(rf))
        u2(cpts,pts,rf,psel)
    elif uchoice == "3":
        print("Computer 1 has chosen move " + str(rf))
        u3(cpts,pts,rf,psel)
    elif uchoice == "4":
        print("Computer 1 has chosen move " + str(rf))
        u4(cpts,pts,rf,psel)
    elif uchoice == "5":
        print("Computer 1 has chosen move " + str(rf))
        u5(cpts,pts,rf,psel)
    elif uchoice == "6":
        print("Computer 1 has chosen move " + str(rf))
        u6(cpts,pts,rf,psel)
    elif uchoice == "7":
        print("**LUCK ZONE**")
        print(storage())
        challenge = input("Put the string shown over in a windows compatible file format and then a wheel will spin to see if you will win or lose this game :")
        if challenge == 's%,Vd62Eel!BnEv6b=4£^cBOTp-LW4FcJO%&,€ghOuAM8!@tsb2-wvOTTiJDN.4Yrv':
            rnd1 = [1,2,3,4,5,6,7,8,9]
            input("If you want to win,you must have number 2 or number 8.Press ENTER to continue")
            rn3 = random.choice(rnd1)
            print("Your number is " + str(rn3))
            if rn3 == 1 or rn3 == 3 or rn3 == 5 or rn3 == 7 or rn3 == 9 or rn3 == 4 or rn3 == 6 :
                print("You lost!")
                cpts = 10
                rps(cpts,pts,psel)
            elif rn3 == 2 or rn3 == 8:
                print("You win!")
                pts = 10
                rps(cpts,pts,psel)
    elif uchoice == "Exit":
        if whowin(310,310,psel) == 'Ended':
            print(whowin(310,310,psel))
            exit()
    elif uchoice == "":
        print("Required parameter missing")
        rps(cpts,pts,psel)
    else:
        print("Invalid parameter : " + uchoice + ".Acceptable values are 1,2,3,4,5,6")
        rps(cpts,pts,psel)
def rps_psel1(cpts,pts,psel):
    if cpts == 10 or pts == 10:
        whowin(cpts,pts,psel)
    print("Player points : " + str(pts))
    print("Player 1 points : " + str(cpts))
    print("Type string 'Exit' to exit the game.")
    print("Player goes first.Next P1")
    uchoice = input("Enter 1,2,3,4,5,6 = ")
    rf = input("P1 : Enter 1,2,3,4,5,6 = ")
    print("Rock...",end='\r')
    time.sleep(0.5)
    print("Rock...Paper...",end='\r')
    time.sleep(0.5)
    print("Rock...Paper...Scissors...",end='\r')
    time.sleep(0.5)
    print("Rock...Paper...Scissors...SHOOT!")
    if uchoice == "1":
        u1(cpts,pts,rf,psel)
    elif uchoice == "2":
        u2(cpts,pts,rf,psel)
    elif uchoice == "3":
        u3(cpts,pts,rf,psel)
    elif uchoice == "4":
        u4(cpts,pts,rf,psel)
    elif uchoice == "5":
        u5(cpts,pts,rf,psel)
    elif uchoice == "6":
        u6(cpts,pts,rf,psel)
    elif uchoice == "7":
        print("**LUCK ZONE**")
        print(storage())
        challenge = input("Put the string shown over in a windows compatible file format and then a wheel will spin to see if you will win or lose this game :")
        if challenge == 's%,Vd62Eel!BnEv6b=4£^cBOTp-LW4FcJO%&,€ghOuAM8!@tsb2-wvOTTiJDN.4Yrv':
            global rn2
            rnd1 = [1,2,3,4,5,6,7,8,9]
            input("If you want to win,you must have number 2 or number 8.Press ENTER to continue")
            rn3 = random.choice(rnd1)
            print("Your number is " + str(rn3))
            if rn3 == 1 or rn3 == 3 or rn3 == 5 or rn3 == 7 or rn3 == 9 or rn3 == 4 or rn3 == 6 :
                print("You lost!")
                cpts = 10
                rps(cpts,pts,psel)
            elif rn3 == 2 or rn3 == 8:
                print("You win!")
                pts = 10
                rps(cpts,pts,psel)
    elif uchoice == "Exit":
        if whowin(310,310,psel) == 'Ended':
            print(whowin(310,310,psel))
            exit()
    elif uchoice == "":
        print("Required parameter missing")
        rps(cpts,pts,psel)
    else:
        print("Invalid parameter : " + uchoice + ".Acceptable values are 1,2,3,4,5,6")
        rps(cpts,pts,psel)
def start():
    print("***RPS - Okmeque1 Edition***")
    print("The INPUT will be shown like this : Enter 1,2,3,4,5,6,any other option to return to start = ")
    print("READ THIS CAREFULLY!!!")
    print("1 = ROCK")
    print("2 = PAPER")
    print("3 = SCISSORS")
    print("4 = ROCK MINER")
    print("5 = CARDBOARD")
    print("6 = BOX KNIFE")
    ps = int(input("Press 1 for SINGLE-PLAYER game or 2 for PLAYER-PLAYER game."))
    if ps == 2:
        ps = 1
        print("Player 2 mode disabled due to a problem.See COMMIT log for more info.")
    input("Press ENTER to continue")
    print("UNCONVENTIONAL RULE SET :")
    print("1 = ROCK can break SCISSORS or BOX KNIFE")
    print("2 = PAPER can break ROCK MINER only.")
    print("3 = SCISSORS can break PAPER only.")
    print("4 = ROCK MINER can break ROCK only.")
    print("5 = CARDBOARD can break ROCK and SCISSORS")
    print("6 = BOX KNIFE can break PAPER and CARDBOARD")
    if rps(0,0,ps) == True:
        rps_psel1(0,0,2)
    rps(0,0,ps)
start()
