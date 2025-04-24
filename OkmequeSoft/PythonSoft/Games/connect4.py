board = [      ["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"],["_","_","_","_","_","_","_"]]
win = False
def play(column,board,player):
    for x in range(6):
        if board[5-x][column] == "_":
            board[5 - x][column] = player
            
            break
def win_or_not(board,player,win):
    for x in range(3):
        for y in range(6):
            if board[y][x] == player and board[y][x + 1] == player and board[y][x + 2] == player and board[y][x + 3] == player:
                print(player + " has won the game and will now close.")
                win = True
                return win
    for x in range(3):
        for y in range(6):
            if board[x][y] == player and board[x + 1][y] == player and board[x + 2][y] == player and board[x + 3][y] == player:
                print(player + " has won the game and will now close.")
                win = True
                return win
    for x in range(3):
        for y in range(4):
            if board[x][y] == player and board[x + 1][y + 1] == player and board[x + 2][y + 2] == player and board[x + 3][y + 3] == player:
                print(player + " has won the game and will now close")
                win = True
                return win
    for x in range(0,3):
        for y in range(1,5):
            if board[x][- y] == player and board[x + 1][- y - 1] == player and board[x + 2][- y - 2] == player and board[x + 3][- y - 3] == player:
                print(player + " has won the game and will now close")
                win = True
                return win
def show_board(board):
    boardstr = ""
    for x in range(6):
        boardstr = ""
        for y in range(7):
            boardstr += board[x][y] + " "
        print(boardstr)
    print("0 1 2 3 4 5 6")



def start():
    while True:
        try:
            show_board(board)
            play(int(input("Enter number of column.0-6 accepted only(any other to abort program.)")),board,"X")
            print("X just played!")
            show_board(board)
            if win_or_not(board,"X",win) == True:
                break
            play(int(input("Enter number of column.0-6 accepted only(any other to abort program.)")),board,"O")
            print("O just played!")
            show_board(board)
            if win_or_not(board,"O",win) == True:
                break
        except ValueError:
            print("STOP : 0211\nCode is either invalid or bad value was specified.")
            input("Press ENTER to exit...")
            return None
        except EOFError or KeyboardInterrupt:
            print("STOP : 0250/0270\nUser has chosen to exit.Exiting...")
            return None
    return
def rules():
    print("The rules of this game is to have 4 of your letters(X or O) to connect with each other either in diagonal,vertical or horizontal.")
    print("You will not win the game if your move is too high(integer overflow) and the program will terminate if wrongly used(not putting the correct integers,putting null or invalid strings)")
    print("This program will skip your turn when you try and make a turn on a column that is already full.There is no revert on this program.All moves are without confirmation and cannot be undone")
    print("We will now return to the main menu")
    start()
def pre_env():
    print("Connect 4 - Okmeque1 Edition")
    print("Please answer 'Y' for yes and 'N'for no")
    A = input("Would you like some extra information before starting this program?")
    if A == "Y":
        rules()
    if A == "N":
        input("Press ENTER to start this game...")
        start()
    
pre_env()
