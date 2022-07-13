import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|",board[0],"|",board[1],"|",board[2],"|",sep="   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|",board[3],"|",board[4],"|",board[5],"|",sep="   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|",board[6],"|",board[7],"|",board[8],"|",sep="   ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
        
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.

    try:
        found = False
        move = int(input("Enter your move: "))
        
        # input must be less than 10 and greater than 0
        while move < 1 or move > 9:
            print("The move is out of range! Choose other move.")
            move = int(input("Enter your move: "))

        while not found:
            # input cannot point to occupied space
            if board[move-1] == move and (board[move-1] != 'O' or board[move-1] != 'X'):    
                board[move-1] = 'O'
                found = True
            else:
                print("The space is already occupied! Choose other move.")
                move = int(input("Enter your move: "))

        display_board(board)
        return move

    except ValueError:
        print("Wrong Input!!! Try Again")
        enter_move(board)
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for i in range(len(board)):
        if board[i] != 'O' and board[i] != 'X':
            free_squares.append(board[i])
    
    return free_squares

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    victory = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in victory:
        if all(y in sign['X'] for y in x):
            print("============================")
            print('Computer has win the GAME!!!')
            print("============================")
            return False

        elif all(y in sign['O'] for y in x):
            print("========================")
            print("You have win the GAME!!!")
            print("    Congratulations!    ")
            print("========================")
            return False

    if make_list_of_free_fields(board) == []:
        print("========================")
        print("     It's a draw!!!     ")
        print("========================")
        return False

    return True

def draw_move(board):
    # The function draws the computer's move and updates the board.
    
    # Find empty position
    free_squares = make_list_of_free_fields(board)
    
    move = random.choice(free_squares)

    for i in range(len(board)):
        if board[i] == move:
            board[move-1] = 'X'

    return move

# setting board
board = [i for i in range(1,10)]

GAME = True
sign = {'X':[],'O':[]}

# computer start with X at the middle
board[5-1] = 'X'
sign['X'].append(5)

while GAME:
    display_board(board)
    sign['O'].append(enter_move(board))
    sign['X'].append(draw_move(board))
    GAME = victory_for(board, sign)

# Final position of the board
display_board(board)
