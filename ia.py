import random
import main


win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def ia(board, difficulty):

    opponent_board = []
    ia_board = []

    for i in range(len(board)):
        if board[i] == 'X':
            opponent_board.append(i + 1)
        elif board[i] == 'O':
            ia_board.append(i + 1)

    random_value = random.randrange(1, 9)

    while True:
        if difficulty == '1': # Play totally random move
            if board[random_value - 1] == ' ':
                return random_value
            elif board:
                random_value = random.randrange(1, 9)
        if difficulty == '2':  # make dumb move 1/5 of the time
            chance = random.random()
            if chance <= 1/5:
                for i in range(len(board)):
                    if board[i] == ' ':
                        return i + 1
            else:
                if board[5 - 1] == ' ':
                    return 5
                else:
                    return predict_futur(opponent_board, ia_board, board)

        if difficulty == '3':  # Always wake best move
            if board[5 - 1] == ' ':
                return 5
            else:
                return predict_futur(opponent_board, ia_board, board)


def predict_futur(enemy_board, ia_board, board):
    temp_futur_enemyboard = []
    temp_futur_enemyboard += enemy_board
    temp_futur_iaboard = []
    temp_futur_iaboard += ia_board
    best_defensive = 0
    best_offensive = 0

    for i in range(len(board)):
        if board[i] == ' ':
            temp_futur_enemyboard.append(i + 1)
            for j in win_combinations:  # Check For counter move
                if are_all_elements_in_list(j, temp_futur_enemyboard) and len(temp_futur_enemyboard) == len(enemy_board) + 1:
                    move = list(set(j).difference(set(enemy_board)).union(set(j).difference(set(enemy_board))))
                    best_defensive = int(move[-1])
                    print(main.colors.FAIL + "\n", "|BEST DEFENSIVE|", "current player position:",
                          enemy_board, "| hypothetical next position:", temp_futur_enemyboard, "| winning cond:", j,
                          "| next_move -->", int(move[-1]), "" + main.colors.ENDC)
                else:
                    temp_futur_enemyboard.clear()
                    temp_futur_enemyboard += enemy_board
                    temp_futur_enemyboard.append(i + 1)
            temp_futur_iaboard.append(i + 1)
            for j in win_combinations:  # Check If for win move
                if are_all_elements_in_list(j, temp_futur_iaboard) and len(temp_futur_iaboard) == len(ia_board) + 1:
                    move = list(set(j).difference(set(ia_board)).union(set(j).difference(set(ia_board))))
                    best_offensive = int(move[-1])
                    print(main.colors.OKGREEN + "\n", "|BEST OFFENSIVE|", "current position:", ia_board, "| hypothetical next position:",
                          temp_futur_iaboard, "| winning cond:", j, "| next_move -->", int(move[-1]), "" + main.colors.ENDC)
                else:
                    temp_futur_iaboard.clear()
                    temp_futur_iaboard += ia_board
                    temp_futur_iaboard.append(i + 1)
    if best_offensive != 0:
        return best_offensive
    if best_defensive != 0:
        return best_defensive
    else:
        if (board[0] == "X" and board[8] == "X") or (board[2] == "X" and board[6] == "X"):
            return 4
        for i in [1, 3, 7, 9]:  # If no counter or win moves then choose a corner and if no corner left put in any blank space
            if board[i - 1] == ' ':
                return i
        for i in range(len(board)):
            if board[i] == ' ':
                return i + 1


def are_all_elements_in_list(list1, list2):
    return all(x in list2 for x in list1)