import random

win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

def ia(board, difficulty):

    opponent_board = []
    ia_board = []

    for i in range(len(board)):
        if board[i] == 'X':
            opponent_board.append(i + 1)
        elif board[i] == 'O':
            ia_board.append(i + 1)

    good_value = False
    random_value = random.randrange(1, 9)

    predict_futur(opponent_board, ia_board)
    while not good_value:
        if difficulty == '1':
            if board[random_value - 1] == ' ':
                good_value = True
                return random_value
            elif board:
                random_value = random.randrange(1, 9)
                print(random_value)
        if difficulty == '3':
            if board[5 - 1] == ' ':
                return 5
            else:
                for i in [1, 3, 7, 9]:
                    if board[i - 1] == 'X' and board[i] == ' ':
                        return i + 1
                    if board[i - 1] == ' ':
                        return i
                    else:
                        print("no move")


def predict_futur(enemy_board, ia_board):
    temp_futur_enemyboard = []
    for i in win_combinations:
        for j in enemy_board:
            if j in i:
                for y in list(set(i).intersection(ia_board)):
                    if y in list(set(i).difference(enemy_board)):
                        print(i)
                    else:
                        print(list(set(i).difference(enemy_board)))