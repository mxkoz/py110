INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINNING_SCORE = 5
WINNING_LINES = [
  [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows
  [1, 4, 7], [2, 5, 8], [3, 6, 9], # columns
  [1, 5, 9], [3, 5, 7]             # diagonals
]
SQUARE_FIVE = '5'

import random
import os

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def display_board(board):
    os.system('clear')
    prompt(f'you are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |   {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |   {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |   {board[9]}')
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}

def prompt(message):
    print(f'==> {message}')

def join_or(list, middle_separator=', ', final_separator=' or '):
    new_str = ''
    for num in range(0, len(list)):
        if num < [len(list)-1]:
            new_str += list[num]
            new_str += middle_separator
        elif num == (len(list) -1):
            new_str += final_separator
            new_str += list[num]


def player_chooses_square(board):
    #valid square choices are those board keys whose values are spaces
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square ({', '.join(valid_choices)}):')
        square = input().strip()
        if square in valid_choices:
            break
        prompt("Sorry that's not a valid choice")
    board[int(square)] = HUMAN_MARKER

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = None
    for line in WINNING_LINES:
        square = find_at_risk_square(line, board, COMPUTER_MARKER)
        if square:
            break
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break
    if not square: 
        if board[5] == INITIAL_MARKER:
            square = SQUARE_FIVE
        else:
            square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def find_at_risk_square(line, board, marker):
     markers_in_line = [board[square] for square in line]
     if markers_in_line.count(marker) == 2:
         for square in line:
             if board[square] == INITIAL_MARKER:
                 return square
     return None
     

def board_full(board):
    return (len(empty_squares(board)) == 0)

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for line in winning_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
            and board[sq2] == HUMAN_MARKER
            and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
            and board[sq2] == COMPUTER_MARKER
            and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

def someone_won(board):
    return bool(detect_winner(board))

def play_tic_tac_toe():
    player_score = 0
    computer_score = 0
    while True:
        board = initialize_board()
        while True:
            display_board(board)

            player_chooses_square(board)
            if detect_winner(board):
                winner = detect_winner(board)
                if winner == 'Player':
                    player_score += 1
                break

            if board_full(board):
                break

            computer_chooses_square(board)
            if detect_winner(board):
                winner = detect_winner(board)
                if winner == 'Computer':
                    computer_score += 1
                break
            if board_full(board):
                break

        if someone_won(board):
            prompt(f"{detect_winner(board)} won!. Player {player_score}, Computer {computer_score}")
        else:
            prompt("It's a tie!")
        
        if player_score == 5 or computer_score == 5:
            prompt(f'Thank you for playing. Final score: Player {player_score}, Computer {computer_score}')
            break

        prompt("Play again? (y or n)")

        answer = input().lower()
        if answer[0] != 'y':
            break

play_tic_tac_toe()
