import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. 
# it is only used to reset the board to blank.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(file_name):
    '''Read the previously existing board from the file if it exists.'''

    # Try to read from json file.
    try:
        with open(file_name, 'rt') as file_handle:
            json_data = file_handle.read()
            dictionary_data = json.loads(json_data)
        return dictionary_data
    
    # If file cannot be found return a blank board, new file will be created when finished playing.
    except FileNotFoundError:
        print(f'Could not open file {file_name}')
        return blank_board["board"][:]
    

def save_board(file_name, board):
    '''Save the current game to a file.'''

    # Try saving the board to the file.
    try:
        with open(file_name,"wt") as file_handle:
            json_data = json.dumps(board)
            file_handle.write(json_data)

    # Display error if the file cannot be opened. 
    except FileNotFoundError:
        print(f'Could not open file {file_name}')

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''

    print('Enter \'q\' to suspend your game. Otherwise, enter a number from 1 to 9')
    print("where the following numbers correspond to the locations on the grid:")
    print(f" 1 | 2 | 3 ")
    print(f"---+---+---")
    print(f" 4 | 5 | 6 ")
    print(f"---+---+---")
    print(f" 7 | 8 | 9 \n")
    print("The current board is:")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def is_x_turn(board):
    '''Determine whose turn it is.'''

    # Initialize players mark counters.
    x_number = 0
    O_number = 0

    # Iterate through board counting marks.
    for box in board:
        if (box == 'X'):
            x_number +=1
        elif (box == 'O'):
            O_number +=1

    # Decide turn based on number of marks.
    if (x_number <= O_number):
        return True
    return False

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''

    # Initialize play to true.
    play = True
    while play:

        # Dispay the board each iteration.
        display_board(board)

        # Deturmine whos turn it is.
        turn = X if is_x_turn(board) else O

        # Get player input.
        user_input = input(f'{turn}> ')

        # Suspend game if player enters q.
        if (user_input == 'q'):
            return board
        else:

            # Convert player input to board location.
            square = int(user_input)-1

            # Only place if the space is empty.
            if (board[square] == BLANK):
                board[square] = turn

            # Check if the game is over.
            if (game_done(board)):

                # Print the final board state.
                print("The final board is:")
                print(f" {board[0]} | {board[1]} | {board[2]} ")
                print(f"---+---+---")
                print(f" {board[3]} | {board[4]} | {board[5]} ")
                print(f"---+---+---")
                print(f" {board[6]} | {board[7]} | {board[8]} \n")
                print(f"The game was won by", turn)

                # Reset and return the board.
                board = blank_board['board']
                return board

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False


def main():
    '''Main Function'''

    # Initialize board
    game_board = read_board('board.json')

    # Save the current board after done playing.
    board = play_game(game_board)
    save_board('board.json',board)

if __name__ == "__main__":

    main()