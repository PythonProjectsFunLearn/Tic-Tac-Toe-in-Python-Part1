from game_back_end import GAME

GAME = GAME()

PLAYER1 = 1
PLAYER2 = 2
played_positions = []

game_matrix = GAME.game_matrix()
game_pos = GAME.position_dictionary()


def print_game(g_matrix):
    print(f'{g_matrix[0][0]} | {g_matrix[0][1]} | {g_matrix[0][2]}\n'
          f'---------\n'
          f'{g_matrix[1][0]} | {g_matrix[1][1]} | {g_matrix[1][2]}\n'
          f'---------\n'
          f'{g_matrix[2][0]} | {g_matrix[2][1]} | {g_matrix[2][2]}')


while True:
    played = input('PLAYER_1 please enter a number! ')
    x, y = game_pos[played]
    if played not in played_positions:
        game_matrix[x][y] = PLAYER1
        played_positions.append(played)
    print_game(game_matrix)
    if GAME.game_status(game_matrix) != 'game_on':
        break
    else:
        played = input('PLAYER_2 please enter a number! ')
        x, y = game_pos[played]
        if played not in played_positions:
            game_matrix[x][y] = PLAYER2
            played_positions.append(played)
        print_game(game_matrix)
        if GAME.game_status(game_matrix) != 'game_on':
            break
