from tictactoe_art import logo, instruction_art
import random

print(logo)
print("ABOUT\nTic-tac-toe is a two-player game, that is played on a 3×3 square grid. Each player occupies a "
      "cell in turns, with the objective of placing three marks in a horizontal, vertical, or diagonal pattern. "
      "One player uses cross 'X' as his marker, while the other uses a naught 'O'.\n\n")
print("INSTRUCTIONS\nTo play this game is very easy, you first need to choose if you want to play agaisnt the "
      "computer or against a friend. Then you will pick if you want to play with 'X' or 'O'. Lastly, you will pick a "
      "number between 1 and 9. The numbers represent the position you want to move:")
print(instruction_art)

# Store the board
the_board = {1: " ", 2: " ", 3: " ",
             4: " ", 5: " ", 6: " ",
             7: " ", 8: " ", 9: " "}


# Function to print the Tic-Tac-Toe board
def print_board(board):
    print('\t ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('\t-----------')
    print('\t ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('\t-----------')
    print('\t ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print("\n")


# Function to print the score-board
def print_scoreboard(score_board):
    print("\t---------------------------------------")
    print("\t              SCOREBOARD              ")
    print("\t---------------------------------------")

    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])

    print("\t---------------------------------------\n")


def player2(num_players):
    """ Define if player 2 will be randomised or another player """
    if num_players == 1:
        player = "Computer"
        return player
    elif num_players == 2:
        print("Player 2")
        player = input("Enter a name:  ")
        print("\n")
        return player
    else:
        print("This is not a valid entry. Please, try again!")


def win_game(player_pos, actual_player):
    winning_possibilities = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for combination in winning_possibilities:
        if all(number in player_pos[actual_player] for number in combination):
            # If all the numbers in combination are in player positions, return True
            return True
    # If not all number in combination are in player positions, return False
    return False


def tie_game(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


def game_round(cur_play, choice_players):
    # Store the positions
    player_position = {'X': [], 'O': []}

    # Loop for the round game
    while True:
        # Determine who's the current PLAYER
        cur_player = choice_players[cur_play]

        print_board(board=the_board)

        # Determine move for computer and players
        if cur_player == "Computer":
            print("Computer's turn.")
            move = random.randint(1, 9)
        else:
            try:
                move = int(input(f"{cur_player}'s turn. Where do you want to move?  "))
            except ValueError:
                print("Invalid entry. Please, try again!")
                continue

        # Check if users entry is a valid number for the game
        if move < 1 or move > 9:
            print("Invalid entry. Please, try again!")
            continue

        # Check if the box to be moved is empty
        if the_board[move] != " ":
            print("Place already filled. Please, try again!")
            continue

        # Update the board
        the_board[move] = cur_play

        # Update the player's position
        player_position[cur_play].append(move)

        # Check if there's a winner
        if win_game(player_pos=player_position, actual_player=cur_play):
            print_scoreboard(score_board=the_board)
            print(f"{cur_player} has won the game!\n")
            return cur_play

        # Check if it's a tie
        if tie_game(player_pos=player_position):
            print_scoreboard(score_board=the_board)
            print("It's a tie")
            return "tie"

        # Switch player moves
        if cur_play == 'X':
            cur_play = 'O'
        else:
            cur_play = 'X'


if __name__ == "__main__":
    # Update the board_keys
    board_keys = []
    for key in the_board:
        board_keys.append(key)

    print("\nHow many players will play?")
    number_of_players = int(input("Type 1 to play against the computer, or 2 to play against a friend:  "))

    player_2 = player2(num_players=number_of_players)

    print("Player 1")
    player_1 = input("Enter a name: ")
    print("\n")

    # Game starts with player 1, but keep changing as the games goes on.
    current_player = player_1

    # Stores the choice of players
    player_choice = {'X': "", 'O': ""}

    # Stores the options
    options = ['X', 'O']

    # Stores the scoreboard
    scoreboard = {player_1: 0, player_2: 0}
    print_scoreboard(score_board=scoreboard)

    # Loop to keep the game going
    while True:
        # Defining player 1 as the one to pick when playing against the computer
        if current_player == "Computer":
            choice = random.randint(1, 2)
        else:
            # Validating users entry
            try:
                print("Time to choose for ", current_player)
                choice = int(input("Enter 1 for 'X'; 2 for 'O'; or 3 to quit the game:  "))
            except ValueError:
                print("Invalid entry. Please, try again!")
                continue

        # Storing players choice
        if choice == 1:
            player_choice['X'] = current_player
            if current_player == player_1:
                player_choice['O'] = player_2
            else:
                player_choice['O'] = player_1
        elif choice == 2:
            player_choice['O'] = current_player
            if current_player == player_1:
                player_choice['X'] = player_2
            else:
                player_choice['X'] = player_1
        elif choice == 3:
            print("\nGood game!\nFinal score:")
            print_scoreboard(score_board=scoreboard)
            break
        else:
            print("Invalid entry. Please, try again!")

        # Stores the winner and pass the variables to the round_game function
        check_winner = game_round(cur_play=options[choice - 1], choice_players=player_choice)

        # Edits the scoreboard according to the winner
        if check_winner != "tie":
            player_won = player_choice[check_winner]
            scoreboard[player_won] = scoreboard[player_won] + 1

        # Clean the board by the end of the game
        for key in board_keys:
            the_board[key] = " "

        print_scoreboard(score_board=scoreboard)

        # Switch player who chooses X or O
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1



