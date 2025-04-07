
class SmallBoard:
    def __init__(self):
        self.cells =  [' ' for _ in range(9)]
        self.winner = None

    def check_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if all(self.cells[i] == player for i in combo):
                self.winner = player
                return
        if_full = self.is_full()
        if if_full:
            self.winner = 'D'

    def is_full(self):
        return all(cell != ' ' for cell in self.cells)

    def is_active(self):
        return self.winner is None

class UltimateTicTacToe:
    def __init__(self):
        self.boards = [SmallBoard() for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.active_board = None

    def diplay(self):
        print()
        for big_row in range(3):
            for small_row in range(3):
                row = []
                for big_col in range(3):
                    board_index = big_row * 3 + big_col
                    board = self.boards[board_index]
                    row_cells = board.cells[small_row*3:(small_row+1)*3]
                    row.append('  |  '.join(row_cells))
                print(' || ')
            if big_row < 2:
                print('=')
        print()

    def is_draw(self):
        return all(board.winner is not None for board in self.boards) and self.winner is None

    def play(self):
        is_draw = self.is_draw()
        while self.winner is None and not is_draw:
            self.diplay()
            print(f'Zaidejas {self.current_player} turi ejima. ')
            if self.active_board is not None:


game = UltimateTicTacToe()
game.diplay()




# def print_board():
#     print()
#     for i in range(3):
#         row = board[i*3:(i+1)*3]
#
#         print (' | '.join(row))
#         if i < 2:
#             print('--+---+--')
#     print()
#
#
# def check_draw():
#     return all(cell != ' ' for cell in board)
#
#
# def play_game():
#     current_player = 'X'
#
#     while True:
#         print_board()
#
#         try:
#             move = int(input(f'Zaidejas {current_player}, pasirink langeli (1-9):' )) - 1
#         except ValueError:
#             print('Netinkama ivestis. Bandyk dar karta.')
#             continue
#         if move < 0 or move > 8:
#             print('Langelis turi buti nuo 1 iki 9')
#             continue
#
#         if board[move] != ' ':
#             print('Sis langelis uzimtas!')
#             continue
#
#         board[move] = current_player
#
#         is_winner = check_winner(current_player)
#         if is_winner:
#             print_board()
#             print(f'Zaidejas {current_player} laimejo!')
#             break
#
#         is_draw = check_draw()
#         if is_draw:
#             print_board()
#             print('Lygiosios')
#             break
#
#         current_player = 'O' if current_player == 'X' else 'X'
#
# play_game()