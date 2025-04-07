import time
import os
import random
def init():#don't ask where's the board
    board = []
    board.append([0,"A","B","C","D","E","F","G","H","I","J"])
    for x in range(10):
        board.append([x + 1," "," "," "," "," "," "," "," "," "," "])
    b1 = []
    b1.append([0,"A","B","C","D","E","F","G","H","I","J"])
    for x in range(10):
        b1.append([x + 1," "," "," "," "," "," "," "," "," "," "])
    return board,b1
def showboard(board):#Very fast renderer
    for y in board:
        print(y)
def clearscreen():#anti-cheat
    if os.name=='nt':
        os.system('cls')
    else:
        os.system(clear)
    return
def chkmv(vpos,board,pos1,size,lettermap):#don't cheat, naughty naughty!
        if vpos == "V":
            validsize = 10 - int(pos1[1]) + 1
            if size > validsize:
                print("Invalid position! Please try again...")
                return False
        if vpos == "H":
            validsize = 10 - lettermap[pos1[0]] + 1
            if size > validsize:
                print("Invalid position! Please try again...")
                return False            
        if vpos == "V" and board[int(pos1[1])][lettermap[pos1[0]]] == " ":
            for x in range(size):
                if board[int(pos1[1]) + x][lettermap[pos1[0]]] != " ":
                    print("Position taken! Please try again.")
                    return False
        if vpos == "H" and board[int(pos1[1])][lettermap[pos1[0]]] == " ":
            for x in range(size):
                if board[int(pos1[1])][lettermap[pos1[0]] + x] != " ":
                    print("Position taken! Please try again.")
                    return False
        return True
def end():#ummmm, what does this do
    print()
    exit()
#lettermap = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}
def shoot(board,pos1,lettermap,total):#DESTROY YOUR TEAMMATE NOWWWWWW
    shooted = board[int(pos1[1])][lettermap[pos1[0]]]
    valid = ["2","3","4","5"]
    if shooted == " " or shooted == "‼":#wait I already shot this ship?
        print("No ship in position.")#umm, slight calculation error
        return False
    elif shooted in valid:
        print("Part of ship destroyed!")
        total[shooted] += 1
        if total[shooted] == 6:
            shooted = "‼"
            print("Entire Ship destroyed!\nNote : This time, no 3-part ship remain")#might have to fix that one day
        elif total[shooted] == int(shooted):
            shooted = "‼"
            print("Entire Ship destroyed!\nNote : Due to a bug in this revision, a 3-part ship may still remain somewhere in the map.")
        else:
            shooted = "‼"
            return shooted
def storage():
    return 's:<%,Vd62Eel!BnEv6b=4£^cB|OTp-LW4:FcJO%&,€ghOuAM8!@t>sb2-wvOTTiJDN.4Yrv'
def luckzone():#Test your luck
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
                exit()
            else:
                print("YAYYY!!! YOU WON THE GREAT LUCK!!!\n")
                os.system("pause")
                exit()
def game():
    print("© Okmeque1 Software")
    board = init()
    b1 = board[0]#board seperator
    b2 = board[1]
    place(b1)
    clearscreen()
    print("Now P2's turn. ")
    place(b2)
    totalb2 = 0
    totalb1 = 0
    hit = {"2":0,"3":0,"4":0,"5":0}
    hits = {"2":0,"3":0,"4":0,"5":0}
    flag = 0#player flag, 0 if b1 is playing, 1 if b2 is playing
    luck = input("Do you want to take a chance to win the game without playing? Take it now through the luck zone! [Y/N] : ")
    if luck == "Y":
        luckzone()
    while True:
        if flag == 0:
            showboard(b1)
            print("This is your board for player B1")
            if shoot(b2,input("Enter your position to shoot. If you want to shoot a ship on F6, type 'F6' : "), {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10},hit) != False:
                totalb1 += 1
            if totalb1 == 17:#checks for if one player has won, no infinite games please.
                end()
            flag = 1 
            os.system("timeout /t 4 /nobreak")
            clearscreen()
        else:
            print("This is your board for player B2")
            showboard(b2)
            if shoot(b1,input("Enter your position to shoot. If you want to shoot a ship on F6, type 'F6' : "), {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10},hits) != False:
                totalb2 += 1
            if totalb2 == 17:
                end()
            flag = 0    
            os.system("timeout /t 4 /nobreak")
            clearscreen()
def place(board):
    try:
        allowed = [1,2,1,1]
        used = [0,0,0,0]#Just enter a ship size from 2 to 5, ignore the print above it instead of having to enter all the values again.
        lettermap = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}#just because the thing has the top as letters, but python doesn't know that without this.
        while allowed != used:
            print("You have used : " + str(used) + " uses.  The first number is size 2, the 2nd is size 3, 3rd is size 4 and 4th is size 5")
            nxtmove = int(input("Please enter a ship size from 2-5(any invalid option to abort) : "))
            used[nxtmove - 2] += 1
            print("Note that if you answer horizontal F6 with size 2, the ship will occupy squares F6 and G6. For vertical, if answer F6 is given with size 2, the ship will occupy squares F6 & F7.")
            pos1 = input("Enter TOP position on board for where to place it(so if you want your ship to be on F6, you would enter F6, then at the next prompt you will be asked for vertical or horizontal position.) : ")
            vselect = input("[V]ertical or [H]orizontal? : ")
            vselect.upper()
            showboard(board)
            if chkmv(vselect,board,pos1,nxtmove,{"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10}) == True:
                    for x in range(nxtmove):
                        if vselect == "V":
                            board[int(pos1[1]) + x][lettermap[pos1[0]]] = str(nxtmove)#shift characters at show
                        elif vselect == "H":
                            board[int(pos1[1])][lettermap[pos1[0]] + x] = str(nxtmove)
                        else:
                            raise NotImplementedError("3D not implemented. Enter VERTICAL or HORIZONTAL and enter the CORRECT values demanded.")
            showboard(board)
    except ValueError:#fine, i'll enter the correct values
        print("STOP : 0211\nBad value was entered. Next time, please enter the CORRECT values demanded. For your convenience, the program will now restart but all of the values will have to be re-entered.")
        game()
    except NotImplementedError:#new error code?
        print("STOP : 2124\n3D is not a thing in this game! When asked with Horizontal or Vertical, answer one of them. For your convenience, the program will now restart but all of the values will have to be re-entered.")
        game()
    except BaseException:
        print("STOP : 770A\nSomething has happened that this program could not handle. For your convenience, the program will now restart but all of the values will have to be re-entered.")
        game()
game()
