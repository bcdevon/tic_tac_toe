import sys


#variable for board
winner = False
board = [
[' ', ' ', ' ' ],
[' ', ' ', ' ' ],
[' ', ' ', ' ' ],
]
board_two = [
                ['x','o','x'],
                ['o','x','o'],
                ['x','o','x'],
            ]

# def update_board(user_input, character, board):
    

def print_board(board):
    print(f"A{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("------")
    print(f"B{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("------")
    print(f"C{board[2][0]}|{board[2][1]}|{board[2][2]}")
    print(" 1 2 3")

def place_char_on_board(char, user_input):
    char_list = ['A', 'B', 'C']
    #display message if input is not on the board A B C
    if user_input[0] not in char_list:
        print(f"lose a turn {user_input} not on board")
    #display message if input is not on board 1-3
    if int(user_input[1]) >3:
        print(f"lose a turn {user_input} not on board") 
    #check for valid input on board space not taken lose a turn if invalid input
    #place char on board if input is valid
    while int(user_input[1]) <= 3 and user_input[0] in char_list:
        column_number = user_input[1]
        row_letter = user_input[0]
        char_to_index = {'1':0, '2':1, '3':2, 'A':0, 'B':1, 'C':2}
        column_index = char_to_index[column_number]
        row_index = char_to_index[row_letter]
        if board[row_index][column_index] == ' ': 
            board[row_index][column_index] = char
            break 
        elif board[row_index][column_index] != ' ':
             print(f"lose a turn {user_input} is taken")
             break
        
           
def check_for_winner(board):
    winner = False
    #first column 
    if board[0][0] != ' ' and board[0][0] == board[1][0] and board[2][0] == board[0][0]:
        winner = True
    #second column
    if board[0][1] != ' ' and board[0][1] == board[1][1] and board [0][1] == board[2][1]:
        winner = True
    #third column
    if board[0][2] != ' ' and board[0][2] == board[1][2] and board[2][2] == board [0][2]:
        winner = True
    #first row
    if board[0][0] != ' ' and board[0][0] == board[0][1] and board[0][2] == board[0][0]:
        winner = True
    #second row
    if board[1][0] != ' ' and board[1][0] == board[1][1] and board[1][2] == board[1][0]:
        winner = True
    #third row
    if board[2][0] != ' ' and board[2][0] == board[2][1] and board[2][2] == board[2][0]:
        winner = True
    #diagonal start top left
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[2][2] == board[0][0]:
        winner = True
    #diagonal start top right
    if board[0][2] != ' ' and board[0][2] == board[1][1] and board[2][0] == board[0][2]:
        winner = True
    return winner

is_x_turn = True
#loop until there is a winner
while winner == False:
    char = 'x' if is_x_turn else 'o'
    #print board
    print_board(board)
    #print controls
    print(f"{char}'s turn")
    print('Enter row letter followed by column number ex. B1')
    print('Enter q to quit')
    #get user input
    user_input = input()
    #do what user says
    if user_input == 'q':
        sys.exit('game over')
    elif user_input != 'q':
        place_char_on_board(char, user_input)
    #evaluate is there a winner 
    winner = check_for_winner(board)
    is_x_turn = not is_x_turn
# who won
if winner == True:
    print(f"{char} is the winner")
    print_board(board)
#add play again 