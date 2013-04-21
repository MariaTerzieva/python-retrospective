from collections import defaultdict


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    def __init__(self):
        self.board = dict(A1=' ', A2=' ', A3=' ',
                          B1=' ', B2=' ', B3=' ',
                          C1=' ', C2=' ', C3=' ')
        self.last = 'dummy'
        self.status = 'Game in progress.'

    def __str__(self):
        horizontal_line = ' '*2 + '-'*13 + '\n'
        vertical_lines = '%s |' + ' %s |'*3 + '\n'
        rows = defaultdict(str)

        for i in range(1, 4):
            rows[i] = vertical_lines % (i, self.board['A' + str(i)],
                                        self.board['B' + str(i)],
                                        self.board['C' + str(i)])

        result = ('\n' + horizontal_line +
                  rows[3] +
                  horizontal_line +
                  rows[2] +
                  horizontal_line +
                  rows[1] +
                  horizontal_line + ' '*4 + 'A   B   C  \n')

        return result

    def __getitem__(self, key):
        return self.board[key]

    def __setitem__(self, key, value):
        if key not in self.board:
            raise InvalidKey
        elif value != 'X' and value != 'O':
            raise InvalidValue
        elif self.board[key] != ' ':
            raise InvalidMove
        elif self.last == value:
            raise NotYourTurn
        self.last = value
        self.board[key] = value
        self.winner()

    def winner(self):
        winning_combinations = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'],
                                ['A3', 'B3', 'C3'], ['A1', 'A2', 'A3'],
                                ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
                                ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]

        def all_equal(list):
            return list == [list[0]] * len(list)

        for combination in winning_combinations:
            if (self.board[combination[0]] != ' ' and
                all_equal([self.board[i] for i in combination]) and
                    self.status == 'Game in progress.'):
                self.status = '%s wins!' % self.board[combination[0]]

    def game_in_progress(self):
        for key, value in self.board.items():
            if value == ' ':
                return True
        return False

    def game_status(self):
        if (self.status != 'X wins!' and self.status != 'O wins!' and
                not self.game_in_progress()):
            self.status = 'Draw!'
        return self.status
