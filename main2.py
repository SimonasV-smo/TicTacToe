# Sukuriame 9 mažas lentas (3x3) ir didelę lentą
small_boards = [[' ' for _ in range(9)] for _ in range(9)]
large_board = [' ' for _ in range(9)]

# Spausdina mažas lentas su standartinėmis linijomis
def print_small_boards():
    print()
    for big_row in range(3):  # Didelių lentų eilės
        for small_row in range(3):  # Mažų lentų eilės
            row = []
            for big_col in range(3):  # Didelių lentų stulpeliai
                start = small_row * 3
                cells = small_boards[big_row * 3 + big_col][start:start + 3]
                row.append(' | '.join(cells))
            print(' || '.join(row))  # Vizualus mažų lentų atskyrimas
        if big_row < 2:
            print('=' * 39)  # Linija tarp didelių lentų
    print()

# Spausdina didelę lentą su dvigubomis linijomis
def print_large_board():
    print("\nDidelės lentos būsena:")
    print(f"{large_board[0]} || {large_board[1]} || {large_board[2]}")
    print("==||===||==")
    print(f"{large_board[3]} || {large_board[4]} || {large_board[5]}")
    print("==||===||==")
    print(f"{large_board[6]} || {large_board[7]} || {large_board[8]}")
    print()

# Tikrina mažos arba didelės lentos laimėjimus
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Žaidimo logika
def play_game():
    current_player = 'X'
    current_board = 4  # Pradedame nuo centrinės lentos

    while True:
        print_small_boards()
        print_large_board()
        print(f'Žaidžiama mažoje lentoje: {current_board + 1}')

        try:
            move = int(input(f'Žaidėjas {current_player}, pasirink langelį (1-9): ')) - 1
        except ValueError:
            print('Netinkama įvestis. Bandykite dar kartą.')
            continue
        if move < 0 or move > 8 or small_boards[current_board][move] != ' ':
            print('Netinkamas ėjimas! Bandykite dar kartą.')
            continue

        small_boards[current_board][move] = current_player

        # Tikriname, ar žaidėjas laimėjo mažą lentą
        if check_winner(small_boards[current_board], current_player):
            large_board[current_board] = current_player

        # Tikriname, ar žaidėjas laimėjo didelę lentą
        if check_winner(large_board, current_player):
            print_small_boards()
            print_large_board()
            print(f'Žaidėjas {current_player} laimėjo visą žaidimą!')
            break

        # Patikriname, ar lygiosios didelėje lentoje
        if all(cell != ' ' for cell in large_board):
            print_small_boards()
            print_large_board()
            print('Lygiosios visoje lentoje!')
            break

        # Keičiamas žaidėjas ir atnaujinama kita maža lenta
        current_player = 'O' if current_player == 'X' else 'X'
        current_board = move if large_board[move] == ' ' else 4  # Jei lenta laimėta, eik į centrinę lentą

play_game()