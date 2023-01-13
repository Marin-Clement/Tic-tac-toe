import ia

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def tictac_grid(value):
    print("\n")
    # First Line
    print(colors.OKCYAN + "\t┏━━━━━━━┳━━━━━━━┳━━━━━━━┓")
    print("\t┃   {}   ┃   {}   ┃   {}   ┃".format(value[0], value[1], value[2]))
    print("\t┣━━━━━━━╋━━━━━━━╋━━━━━━━┫")
    # Second Line
    print("\t┃   {}   ┃   {}   ┃   {}   ┃".format(value[3], value[4], value[5]))
    print("\t┣━━━━━━━╋━━━━━━━╋━━━━━━━┫")
    # Third Line
    print("\t┃   {}   ┃   {}   ┃   {}   ┃".format(value[6], value[7], value[8]))
    print("\t┗━━━━━━━┻━━━━━━━┻━━━━━━━┛" + colors.ENDC)
    print("\n")


def my_scoreboard(score_board):
    print(colors.OKGREEN + "\t┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫" + colors.ENDC)
    print(colors.OKGREEN + "\t┃            " + colors.FAIL + "SCOREBOARD" + colors.ENDC + "           " + colors.OKGREEN + "┃")
    print("\t┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛" + colors.ENDC)

    list_of_the_two_players = list(score_board.keys())
    print(colors.OKGREEN + "\t", list_of_the_two_players[0] + colors.ENDC)
    print(colors.OKBLUE + "\t", score_board[list_of_the_two_players[0]])
    print(colors.FAIL + "\t", list_of_the_two_players[1] + colors.ENDC)
    print(colors.OKBLUE + "\t", score_board[list_of_the_two_players[1]])

    print(colors.OKGREEN + "\t━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n" + colors.ENDC)


def my_history(history):
    print(colors.OKGREEN + "\t┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓" + colors.ENDC)
    print(colors.OKGREEN + "\t┃             " + colors.FAIL + "HISTORY" + colors.ENDC + "             " + colors.OKGREEN + "┃")
    print("\t┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫" + colors.ENDC)
    for i in range(len(history)):
        print(colors.OKBLUE + "\t", "GAME", i + 1, ":", history[i],)
    print(colors.OKGREEN + "\t┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫" + colors.ENDC)


def win_validate(position_player, current_player):
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for i in win_combinations:
        if all(j in position_player[current_player] for j in i):
            return True
    return False


def tie_validate(position_player):
    if len(position_player['X'] + position_player['O']) == 9:
        return True
    return False


def game_loop(current_player):

    value = [' ' for i in range(9)]

    position_player = {
        'X': [],
        'O': []
    }

    while True:
        tictac_grid(value)

        if game_mode == '2':
            try:
                print(colors.WARNING + "The player", colors.OKBLUE + current_player, colors.WARNING + "turn : ", end="" + colors.ENDC)
                move = int((input()))
            except ValueError:
                print("ERROR in Input, try again!")
                continue

            if move < 1 or move > 9:
                print("Invalid Number Input!!!")
                continue

            if value[move - 1] != ' ':
                print("This is CASE is already fill")
                continue

            value[move - 1] = current_player

        else:
            if current_player == 'X':
                try:
                    print(colors.WARNING + "The player", colors.OKBLUE + current_player, colors.WARNING + "turn : ",
                          end="" + colors.ENDC)
                    move = int((input()))
                except ValueError:
                    print("ERROR in Input, try again!")
                    continue

                if move < 1 or move > 9:
                    print("Invalid Number Input!!!")
                    continue

                if value[move - 1] != ' ':
                    print("This is CASE is already fill")
                    continue
                value[move - 1] = current_player

            else:
                print(colors.WARNING + "IA TURN" + colors.ENDC)
                move = ia.ia(value, difficulty)

                value[move - 1] = current_player

        position_player[current_player].append(move)

        if win_validate(position_player, current_player):
            tictac_grid(value)
            print(colors.OKCYAN + current_player, colors.OKGREEN + "Win !!!" + colors.ENDC)
            print("\n")
            return current_player

        if tie_validate(position_player):
            tictac_grid(value)
            print(colors.OKGREEN + "Tied !!!" + colors.ENDC)
            return 'T'

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


if __name__ == "__main__":

    print(colors.OKGREEN + "Do You want to play against AI or PLAYER")
    print(colors.OKCYAN + "Please press 1 for AI")
    print(colors.OKCYAN + "Please press 2 for PLAYER" + colors.ENDC)
    game_mode = input(colors.WARNING + "Choix: " + colors.ENDC)

    if game_mode == '2':
        print(colors.OKGREEN + "First Player" + colors.ENDC)
        first_player = input(colors.OKCYAN + "First player enter your name: " + colors.ENDC)
        print("\n")

        print(colors.FAIL + "Second Player" + colors.ENDC)
        second_player = input(colors.OKCYAN + "Second player enter your name: " + colors.ENDC)
        print("\n")

        current_player = first_player

        player_choice = {
            'X': [],
            'O': []
        }

        option = ['X', 'O']

        score_board = {first_player: 0,
                       second_player: 0}

        history = []

        my_scoreboard(score_board)

        while True:
            print(colors.OKGREEN + current_player.upper() + ", " + colors.ENDC + "Choice: ")
            print(colors.OKCYAN + "Please press 1 for X")
            print(colors.OKBLUE + "Please press 2 for O")
            print(colors.FAIL + "Please press 3 for Exit" + colors.ENDC)

            try:
                choice = int(input())
            except ValueError:
                print(colors.FAIL + "This input is Invalid!!! Please Try Again\n" + colors.ENDC)
                continue

            if choice == 1:
                player_choice['X'] = current_player
                if current_player == first_player:
                    player_choice['O'] = second_player
                else:
                    player_choice['O'] = first_player

            elif choice == 2:
                player_choice['O'] = current_player
                if current_player == first_player:
                    player_choice['X'] = second_player
                else:
                    player_choice['X'] = first_player

            elif choice == 3:
                print("\t" + colors.OKBLUE + "The final scores are: " + colors.ENDC + "\n")
                my_history(history)
                my_scoreboard(score_board)
                print("\t" + colors.OKBLUE + "Thank For Playing :)" + colors.ENDC)
                break

            else:
                print(colors.FAIL + "This is an Invalid choice!! Please try again\n" + colors.ENDC)

            winner = game_loop(option[choice - 1])

            if winner != 'T':
                player_won = player_choice[winner]
                score_board[player_won] = score_board[player_won] + 1

                if player_won == first_player:
                    history.append(
                        colors.OKGREEN + player_won + colors.WARNING + " - " + colors.FAIL + second_player + colors.ENDC)
                else:
                    history.append(
                        colors.FAIL + first_player + colors.WARNING + " - " + colors.OKGREEN + second_player + colors.ENDC)
                my_history(history)
                my_scoreboard(score_board)
            else:
                history.append(colors.WARNING + first_player + colors.WARNING + " - " + colors.WARNING + second_player + colors.FAIL + " ┃ " + colors.OKBLUE + "TIE" + colors.ENDC)
                my_history(history)
                my_scoreboard(score_board)

            if current_player == first_player:
                player_current = second_player
            else:
                player_current = first_player

    if game_mode == '1':
        print(colors.OKGREEN + "Choose IA difficulty")
        print(colors.OKCYAN + "Please press 1 for EASY")
        print(colors.OKCYAN + "Please press 2 for NORMAL")
        print(colors.OKCYAN + "Please press 3 for HARD" + colors.ENDC)

        difficulty = input(colors.WARNING + "Choix: " + colors.ENDC)

        match difficulty:
            case '1':
                ia_player = "Easy-IA"
            case '2':
                ia_player = "Normal-IA"
            case '3':
                ia_player = "Hard-IA"
            case _:
                ia_player = "IA"

        print(colors.OKGREEN + "Player" + colors.ENDC)
        first_player = input(colors.OKCYAN + "Enter your name: " + colors.ENDC)
        print("\n")

        current_player = first_player

        player_choice = {
            'X': [],
            'O': []
        }

        option = ['X', 'O']

        score_board = {first_player: 0,
                       ia_player: 0}

        history = []

        my_scoreboard(score_board)

        while True:
            print(colors.OKGREEN + "Please press 1 to start" + colors.ENDC)
            print(colors.FAIL + "Please press 2 for Exit" + colors.ENDC)

            try:
                choice = int(input())

            except ValueError:
                print(colors.FAIL + "This input is Invalid!!! Please Try Again\n" + colors.ENDC)
                continue

            if choice == 1:
                player_choice['X'] = first_player
                player_choice['O'] = ia_player

            elif choice == 2:
                print("\t" + colors.OKBLUE + "The final scores are: " + colors.ENDC + "\n")
                my_history(history)
                my_scoreboard(score_board)
                print("\t" + colors.OKBLUE + "Thank For Playing :)" + colors.ENDC)
                break

            else:
                print(colors.FAIL + "This is an Invalid choice!! Please try again\n" + colors.ENDC)
                continue

            winner = game_loop(option[0])

            if winner != 'T':
                player_won = player_choice[winner]
                score_board[player_won] = score_board[player_won] + 1
                if player_won == first_player:
                    history.append(colors.OKGREEN + player_won + colors.WARNING + " - " + colors.FAIL + ia_player + colors.ENDC)
                else:
                    history.append(colors.FAIL + first_player + colors.WARNING + " - " + colors.OKGREEN + ia_player + colors.ENDC)
                my_history(history)
                my_scoreboard(score_board)
            else:
                history.append(colors.WARNING + first_player + colors.WARNING + " - " + colors.WARNING + ia_player + colors.FAIL + " ┃ " + colors.OKBLUE + "TIE" + colors.ENDC)
                my_history(history)
                my_scoreboard(score_board)
            if current_player == first_player:
                player_current = ia_player
            else:
                player_current = first_player
