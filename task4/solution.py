class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class InvalidKey(Exception):
    pass


class NotYourTurn(Exception):
    pass


class TicTacToeBoard:
    BOARD = '''
  -------------
3 | {A3} | {B3} | {C3} |
  -------------
2 | {A2} | {B2} | {C2} |
  -------------
1 | {A1} | {B1} | {C1} |
  -------------
    A   B   C  \n'''

    WINNING_COMBINATIONS = [['A1', 'B1', 'C1'], ['A2', 'B2', 'C2'],
                            ['A3', 'B3', 'C3'], ['A1', 'A2', 'A3'],
                            ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'],
                            ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]

    STATUS_X_WINS = 'X wins!'
    STATUS_O_WINS = 'O wins!'
    STATUS_DRAW = 'Draw!'
    STATUS_GAME_IN_PROGRESS = 'Game in progress.'
    EMPTY = ' '
    X_SIGN = 'X'
    O_SIGN = 'O'
    SLOTS = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')

    def __init__(self):
        self._board = {slot: self.EMPTY for slot in self.SLOTS}
        self._last = self.EMPTY
        self._status = self.STATUS_GAME_IN_PROGRESS

    def __str__(self):
        return self.BOARD.format(**self._board)

    def __getitem__(self, key):
        if key not in self._board:
            raise InvalidKey("Invalid key!")

        return self._board[key]

    def __setitem__(self, key, value):
        if key not in self._board:
            raise InvalidKey("Invalid key!")
        if value != self.X_SIGN and value != self.O_SIGN:
            raise InvalidValue("Invalid value!")
        if self._board[key] != self.EMPTY:
            raise InvalidMove("Invalid move!")
        if self._last == value:
            raise NotYourTurn("Heeey, it's not your turn!")

        self._last = value
        self._board[key] = value
        self.__winner()

    def __winner(self):
        """Check if there is a winner and change board status."""
        def all_equal(list):
            return list[0] != self.EMPTY and list == [list[0]] * len(list)

        if self._status == self.STATUS_GAME_IN_PROGRESS:
            for combination in self.WINNING_COMBINATIONS:
                if all_equal([self._board[i] for i in combination]):
                    if self._board[combination[0]] == self.X_SIGN:
                        self._status = self.STATUS_X_WINS
                    else:
                        self._status = self.STATUS_O_WINS

    def __moves(self):
        return self.EMPTY in self._board.values()

    def game_status(self):
        if self._status == self.STATUS_GAME_IN_PROGRESS and not self.__moves():
            self._status = self.STATUS_DRAW

        return self._status
