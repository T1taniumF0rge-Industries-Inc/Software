import random
import time
num = random.choice([1,2,3,4,5,6])


def dés(score):
    try:
        num = random.choice([1,2,3,4,5,6])
        score = score + num
        print(num)
        if num == 1:
            print("You lost")
            print("The score is " + str(score))
            return
        else:
            print("This is a random based game.If the number is one,you lose.Do you want to continue?[Y,N]")
            a = input("")
            if a == "N":
                print("The score is " + str(score) + ".The game has ended")
            if a == "Y":
                print("Score saved.You will see the score when you lose.")
                dés(score)
    except KeyboardInterrupt or EOFError:
        print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
        return None
def start():
    print("NOT 1 GAME : The computer will choose a number.If the number is 1,you lose the game.")
    print("On easy mode,your score is not reset when you lose,on hard mode,the score is 0 if you lose.")
    print("The creator of this game is Okmeque1")
    A = input('Do you want the easy or hard mode?[E,H]')
    if A == 'E':
        print('Starting game...')
        time.sleep(5)
        dés(0)
    elif A == 'H':
        print('Starting game...')
        time.sleep(5)
        dés1(0)
    else:
        print('Saving the game...')
        time.sleep(10)
        print('Game stopped.')
def dés1(score):
             try:
                num = random.choice([1,2,3,4,5,6])
                score = score + num
                print(num)
                print("The score is " + str(score))
                if num == 1:
                    print("You lost")
                    print("The score is 0")
                    return
                else:
                    print("This is a random based game.If the number is one,you lose.Do you want to continue?[Y,N]")
                    a = input("")
                    if a == "N":
                        print("The score is " + str(score) + ".The game has ended")
                    if a == "Y":
                        
                        dés1(score)
             except KeyboardInterrupt or EOFError:
                 print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
                 return None
start()
