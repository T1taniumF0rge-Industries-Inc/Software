import random
import time
def win_or_not(P1,P2):
    if P1 == 1 and (P2 == 3 or P2 == 6) or P1 == 2 and P2 == 4 or P1 == 3 and P2 == 2 or P1 == 4 and P2 == 1 or P1 == 5 and (P2 == 1 or P2 == 3) or P1 == 6 and (P2 == 2 or P2 == 5):
        input("P1 has gained a point.Press ENTER to continue")
        return "P1"
    if P2 == 1 and (P1 == 3 or P1 == 6) or P2 == 2 and P1 == 4 or P2 == 3 and P1 == 2 or P2 == 4 and P1 == 1 or P2 == 5 and (P1 == 1 or P1 == 3) or P2 == 6 and (P1 == 2 or P1 == 5):
        input("P2 has gained a point.Press ENTER to continue")
        return "P2"
    else:
        input("Nothing happened.Press ENTER to continue...")
        return
def game(P1PTS,P2PTS,CS):
    flag = True
    while flag == True:
        print("P1 Points : " + str(P1PTS))
        print("P2 Points : " + str(P2PTS))
        moves = [1,2,3,4,5,6]
        P1Play = int(input("P1 : Enter a valid move(any invalid option to abort) : "))
        if CS == 1:
            P2Play = random.choice(moves)
        elif CS == 2:
            P2Play = int(input("P2 : Enter a valid move(any invalid option to abort) : "))
        else:
            input("STOP : BAD_VALUE : The value for CS is invalid.This is usually due to user error or the code has been tampered with and will now exit.\nPress ENTER to exit...")
            return None
        if P1PTS == 10:
            print("P1 has won!P2 must restart their computer.")
            return
        if P2PTS == 10:
            print("P2 has won!P1 must restart their computer.")
            return
        print("ROCK...",end='\r')
        time.sleep(0.5)
        print("ROCK...PAPER",end='\r')
        time.sleep(0.5)
        print("ROCK...PAPER...SCISSORS",end='\r')
        time.sleep(0.5)
        print("ROCK...PAPER...SCISSORS...SHOOT!",end='\n')
        print("Computer move = " + str(P2Play) if CS == 1 else "")
        result = win_or_not(P1Play,P2Play)
        if result == "P1":
            P1PTS += 1
        elif result == "P2":
            P2PTS += 1
print("***RPS - Compact Edition***")
print("The INPUT will be shown like this : Enter 1,2,3,4,5,6,any other option to return to start = ")
print("READ THIS CAREFULLY!!!")
print("1 = ROCK")
print("2 = PAPER")
print("3 = SCISSORS")
print("4 = ROCK MINER")
print("5 = CARDBOARD")
print("6 = BOX KNIFE")
try:
    ps = int(input("Press 1 for SINGLE-PLAYER game or 2 for PLAYER-PLAYER game."))
except ValueError:
    print("STOP : 0211\nCode is either invalid or bad value was specified.")
    input("Press ENTER to exit")
    exit()
except KeyboardInterrupt or EOFError:
    print("STOP : 0250/0270\nThe user has chosen to exit.Exiting...")
    exit()
input("Press ENTER to continue")
print("UNCONVENTIONAL RULE SET :")
print("1 = ROCK can break SCISSORS or BOX KNIFE")
print("2 = PAPER can break ROCK MINER only.")
print("3 = SCISSORS can break PAPER only.")
print("4 = ROCK MINER can break ROCK only.")
print("5 = CARDBOARD can break ROCK and SCISSORS")
print("6 = BOX KNIFE can break PAPER and CARDBOARD")
try:
    game(0,0,ps)
except ValueError:
    print("STOP : 0211\nCode is either invalid or bad value was specified.")
    input("Press ENTER to exit")
    exit()
except KeyboardInterrupt or EOFError:
    print("STOP : 0250/0270\nThe user has chosen to exit.Exiting...")
    exit()
