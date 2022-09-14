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

def place_char_on_board():
    column_number = user_input[1]
    row_letter = user_input[0]
    char_to_index = {'1':0, '2':1, '3':2, 'A':0, 'B':1, 'C':2}
    column_index = char_to_index[column_number]
    row_index = char_to_index[row_letter]
    board[row_index][column_index] = 'x'
    print_board(board)

#loop until there is a winner
while winner == False:
    #print board
    print_board(board)
    #print controls
    print('X turn')
    print('Enter row letter followed by column number ex. B1')
    print('Enter q to quit')
    user_input = input()
    if user_input == 'q':
        sys.exit('game over')
    elif user_input != 'q':
        place_char_on_board()
        
    
    #get user input function

    
    #do what user says
    



    
    
    #evaluate is there a winner 

# who won
#add play again 