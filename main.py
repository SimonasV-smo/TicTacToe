
board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]

        print (' | '.join(row))
        if i < 2:
            print('--+---+--')
    print()

def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):


def play_game():
    current_player = 'X'

    while True:
        print_board()

        try:
            move = int(input(f'Zaidejas{current_player}, pasirink langeli (1-9):' )) - 1
        except ValueError:
            print('Netinkama ivestis. Bandyk dar karta.')
            continue
        if move < 0 or move > 8:
            print('Langelis turi buti nuo 1 iki 9')
            continue

        if board[move] != ' ':
            print('Sis langelis uzimtas!')
            continue

        board[move] = current_player

        is_winner = check_winner(current_player)
        if check_winner(current_player):
            print_board()
            print(f'Zaidejas {current_player} laimejo!')
            break


play_game()