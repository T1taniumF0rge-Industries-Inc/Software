board = [["00","01","02"],["10","11","12"],["20","21","22"]]

global flag
flag = True
def show(board):
    for c in range(3):
            print(board[c])            
show(board)
def change(board,b):
    row  = int(input("Enter the first number(e.g if you want to select the row 2(10,11,12) , hit 1).Integers from 0-2"))
    colon = int(input("Enter column number(e.g if you want to select the column 2(01,11,21) , hit 1).Integers from 0-2"))
    if "X" == board[row][colon] or  "O" == board[row][colon]:
        print("Write protect error.Press CTRL-C to abort this program or attempt to write to another integer")
        change(board,b)
    else:
        board[row][colon] = b
        show(board)
def chkend(board,b):
    if board[0][0] + board[0][1] + board[0][2] == b + b + b:
        print(b + " has won the game.")
        return False
    else:
        return(True)
        

def chkend(board,b):
    end_states =[board[0][0] + board[0][1] + board[0][2],
                 board[1][0] + board[1][1] + board[1][2],
                 board[2][0] + board[2][1] + board[2][2],
                 board[0][0] + board[1][0] + board[2][0],
                 board[0][1] + board[1][1] + board[2][1],
                 board[0][2] + board[1][2] + board[2][2],
                 board[0][0] + board[1][1] + board[2][2],
                 board[0][2] + board[1][1] + board[2][0]]
    if b + b + b in end_states:
        print(b + " has won the game.")
        return False
    else:
        return(True)
        


    
count = 0
while flag == True:
    try:
        if count == 9:
            print("A draw has occured and you will need to rerun this program.")
            print("This program has been halted")
            flag = False
        change(board,"O")
        count += 1
        flag = chkend(board,"O")
        print(count)
        if count == 9:
            print("A draw has occured and you will need to rerun this program.")
            print("This program has been halted")
            flag = False
        
        if flag == True:
            change(board,"X")
            count += 1
            flag = chkend(board,"X")
    except ValueError:
        print("STOP : 0211\nCode is either invalid or bad value was specified")
        input("Press ENTER to exit...")
        exit()
    except KeyboardInterrupt or EOFError:
        print("STOP : 0250\nUser has chosen to exit.Exiting...")
        exit()
#return false
#count = count + 1
