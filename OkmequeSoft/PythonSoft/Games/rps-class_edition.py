from getpass import getpass#starting imports
from os import system,name
import random
class RPS:
    def __init__(self,limit):
        self.pts1 = 0#points
        self.pts2 = 0
        self.limit = limit#points limit. If you're crazy you can do it up to the 64-bit integer limit. but you'll probably die before a 16th of a game occurs
    def endchk(self):
                if self.pts1 == self.limit or self.pts2 == self.limit:#can't go on forever blud
                    print(f"Congratulations to P{current} for winning. ")
                    input("Press ENTER to EXIT...")
                    exit()
    def clearscreen(self):#make it look nicer for the UI
        if name == 'nt':
            system("cls")
        else:
            system("clear")
    def move(self,mov,mov2,current,computer,rndmov):
        if computer == True:
            mov2 = rndmov# if computer is enabled the program ignores what is mov2 and sets mov2 to random move
        pointdict = {1:[3,6], 2:[4], 3:[2], 4:[1], 5:[1,3], 6:[2,5]}#map to win!
        if mov in pointdict:
            if mov2 in pointdict[mov]:
                if current == 1:
                    self.pts1 += 1
                else:
                    self.pts2 += 1         
                print(f"Current points : \nP1 : {self.pts1}\nP2 : {self.pts2}")      
                input(f"P{current} has gained a point. Press ENTER to continue...")
                self.clearscreen()
                if current == 1:
                    return self.pts1
                else:
                    return self.pts2
            else:
                print(f"Current points : \nP1 : {self.pts1}\nP2 : {self.pts2}")  
                input("Nothing happened. Press ENTER to continue...")
                self.clearscreen()
                return
        else:
            print(f"Current points : \nP1 : {self.pts1}\nP2 : {self.pts2}")  
            input("Nothing happened. Press ENTER to continue...")
            self.clearscreen()
            return 
    def rungame(self,computer):#god damn computer making it unclean
        print("WARNING! It is normal that you don't see what you are typing, as a security measure. If you are unsure of what you typed, hold the BACKSPACE key for 15 seconds or press CTRL-C to terminate the program.\nEven if computer mode is enabled, you MUST enter a move for P2. If not, the program could terminate!")
        p1mov = int(getpass("Enter P1 move from 1-6. Enter 7 to see move manual. If this is not respected the program could terminate with no warning! : "))
        p2mov = 0
        if computer == False:
            p2mov = int(getpass("Enter P2 move from 1-6. Enter 7 to see move manual. If this is not respected the program could terminate with no warning! : "))
        if p1mov == 7 or p2mov == 7:
            print("UNCONVENTIONAL RULE SET :")
            print("1 = ROCK can break SCISSORS or BOX KNIFE")
            print("2 = PAPER can break ROCK MINER only.")
            print("3 = SCISSORS can break PAPER only.")
            print("4 = ROCK MINER can break ROCK only.")
            print("5 = CARDBOARD can break ROCK and SCISSORS")
            print("6 = BOX KNIFE can break PAPER and CARDBOARD")
            p1mov = int(getpass("Enter P1 move from 1-6. Enter 7 to see move manual. If this is not respected the program could terminate with no warning! : "))
            if computer == False:
                p2mov = int(getpass("Enter P2 move from 1-6. Enter 7 to see move manual. If this is not respected the program could terminate with no warning! : "))
        print(f"P1's move was {p1mov}\nP2's move was {p2mov}")
        return p1mov, p2mov
game = RPS(int(input("Please enter maximum points value : ")))
current = 1
computer = input("Do you want to play against a computer? [Y/N] : ")
computer.upper()
compmap = {"Y":True,"N":False}
computer = compmap[computer]
while True:
        P1Mov, P2Mov = game.rungame(computer)
        if current == 1:
            rndmov = random.randint(1,6)
            game.move(P1Mov, P2Mov, current,computer,rndmov)
            game.endchk()
            current = 2
        else:
            rndmov = random.randint(1,6)
            game.move(P2Mov, P1Mov, current,computer,rndmov)
            game.endchk()
            current = 1
