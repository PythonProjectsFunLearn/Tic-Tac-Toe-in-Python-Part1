class GAME:

    @staticmethod
    def game_matrix():
        return [list(0 for _ in range(3)) for _ in range(3)]

    @staticmethod
    def position_dictionary():
        return {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2)
                }

    @staticmethod
    def game_status(game):
        if game[0][0] == game[0][1] == game[0][2] != 0:
            return 'X' if game[0][0] == 1 else 'O'
        elif game[1][0] == game[1][1] == game[1][2] != 0:
            return 'X' if game[1][0] == 1 else 'O'
        elif game[2][0] == game[2][1] == game[2][2] != 0:
            return 'X' if game[2][0] == 1 else 'O'
        elif game[0][0] == game[1][0] == game[2][0] != 0:
            return 'X' if game[0][0] == 1 else 'O'
        elif game[0][1] == game[1][1] == game[2][1] != 0:
            return 'X' if game[0][1] == 1 else 'O'
        elif game[0][2] == game[1][2] == game[2][2] != 0:
            return 'X' if game[0][2] == 1 else 'O'
        elif game[0][0] == game[1][1] == game[2][2] != 0:
            return 'X' if game[0][0] == 1 else 'O'
        elif game[0][2] == game[1][1] == game[2][0] != 0:
            return 'X' if game[0][2] == 1 else 'O'

        for i in game:
            if 0 in i:
                return 'game_on'

        return 'game_over'

    def check_for_tie(self, game, next_player):
        available_moves = 0
        for i in game:
            for j in i:
                if j == 0:
                    available_moves += 1

        if available_moves > 1:
            return False
        elif available_moves == 1:
            for i in range(3):
                for j in range(3):
                    if game[i][j] == 0:
                        game[i][j] = next_player

            return True if self.game_status(game) == "game_over" else False
