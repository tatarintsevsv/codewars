#https://www.codewars.com/kata/59de9f8ff703c4891900005c
import numpy as np

class Go:
    _int_board = []
    moves = {True: 'x', False: 'o'}
    _verbose = False

    def __init__(self, size, size2=-1):
        n, m = 100, 100
        if type(size) == int:
            n, m = size, size
        if type(size) == str:
            m, n = size.split('X')
        if size2 != -1:
            m, n = size, size2
        if self._verbose:
            print(f'game = Go({m}, {n})')
        if int(n) > 25 or int(m) > 25:
            raise NameError('incorrect size')
        self._int_board = [['.'] * int(n) for x in range(int(m))]
        self.moveX = True
        self.history = []
        self.game_started = False
        self.push()


    @property
    def turn(self):
        return 'black' if self.moveX else 'white'

    @property
    def size(self):
        return {"height": int(len(self._int_board)), "width": int(len(self._int_board[0]))}

    @property
    def board(self):
        return np.flip(self._int_board, axis=0).tolist()

    @board.setter
    def board(self, value):
        self._int_board = value

    def print(self, tbl = None):
        if not tbl:
            tbl = self._int_board
        print('   A B C D E F G H J K L M N O P Q R S T U V W X Y Z'[:len(tbl[0]) * 2 + 2])
        for i in range(len(tbl)):
            print(f'{i + 1}{" " if i < 9 else ""} {"|".join(tbl[i])}')
        print('\n')

    def get_coords(self, s):
        mi, mj = s[:-1], s[-1]
        mi, mj = int(mi) - 1, int(ord(mj) - ord('A'))
        if mj > 8:
            mj -= 1
        if mi >= len(self._int_board) or mj >= len(self._int_board[0]):
            raise NameError('Index out of bounds', s)
        return mi, mj

    def _int_pass_turn(self):
        self.game_started = True
        self.moveX = not self.moveX


    def pass_turn(self):
        if self._verbose:
            print('game.pass_turn()')
        self._int_pass_turn()
        self.push()

    def reset(self):
        self.__init__(len(self._int_board), len(self._int_board[0]))


    def push(self):
        rec = [[x for x in l] for l in self._int_board]
        self.history.append(rec)

    def rollback(self, n=1, old = True):
        if self._verbose:
            print(f'game.rollback({n})')
        self._int_rollback(n)

    def _int_rollback(self, n=1, changePass=True):
        while n > 0 and len(self.history)>1:
            n -= 1
            self._int_board = self.history.pop()
            if changePass:
                self.moveX = not self.moveX
        if n > 0:
            raise NameError('moo many rollbacks')

    def handicap_stones(self, n):
        if self.game_started:
            raise NameError('its too late to set handicap')
        self.game_started = True
        if len(self._int_board) != len(self._int_board[0]) or len(self._int_board) not in (9, 13, 19):
            raise NameError('invalid _int_board size')

        if len(self._int_board) == 9:
            g = '....................2...3...............5...............4...1....................'
            if n > 5:
                raise NameError('Too mutch handicap')
        if len(self._int_board) == 13:
            g = '..........................................2..9..3................................6..5..7................................4..8..1..........................................'
            if n > 9:
                raise NameError('Too mutch handicap')
        if len(self._int_board) == 19:
            g = '............................................................2.....9.....3.....................................................................................................6.....5.....7.....................................................................................................4.....8.....1............................................................'
            if n > 9:
                raise NameError('Too mutch handicap')

        for i in range(1, 10):
            if i <= n:
                g = g.replace(str(i), 'x')
            if i > n:
                g = g.replace(str(i), '.')
        for i in range(len(self._int_board)):
            for j in range(len(self._int_board)):
                self._int_board[i][j] = g[i * len(self._int_board) + j]

    def fill_shape(self, mi, mj, fill=False):
        res = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (abs(di) + abs(dj) == 2) or (di == 0 and dj == 0):
                    continue
                if mi + di not in range(len(self._int_board)) or mj + dj not in range(len(self._int_board[0])):
                    continue
                if self._int_board[mi + di][mj + dj] == '.':
                    res += 1
                if self._int_board[mi + di][mj + dj] != self.moves[not self.moveX]:
                    continue
                self._int_board[mi + di][mj + dj] = '#'
                res = res + self.fill_shape(mi + di, mj + dj)
        return res

    def KO_check(self):
        if len(self.history) < 4:
            return False
        res = np.array_equal(np.matrix(self._int_board), np.matrix(self.history[-2]))
        if res:
            self._int_rollback(3, changePass=False)
        return res

    def take(self, mi, mj):
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if mi + di not in range(len(self._int_board)) or mj + dj not in range(len(self._int_board[0])):
                    continue
                if self._int_board[mi + di][mj + dj] == self.moves[not self.moveX]:
                    self.push()
                    self._int_board[mi + di][mj + dj] = '#'
                    freedom = self.fill_shape(mi + di, mj + dj)
                    if freedom == 0:
                        self.history.pop()
                        self._int_board = [['.' if x == '#' else x for x in l] for l in self._int_board]
                    else:
                        self._int_rollback(changePass=False)
                        self._int_board[mi + di][mj + dj] = self.moves[not self.moveX]


    def move(self, *movelist):
        self.game_started = True
        if len(movelist) == 0:
            return
        if len(movelist) > 1:
            for a in movelist:
                self.move(a)
            return
        else:
            move = movelist[0]
        if move == '':
            self._int_pass_turn()
            return
        if self._verbose:
            print(f'game.move("{move}")')
        self.push()
        mi, mj = self.get_coords(move)
        if self._int_board[mi][mj] == '.':
            self.push()
            self._int_board[mi][mj] = '#'
            self._int_rollback(changePass=False)
            self._int_board[mi][mj] = self.moves[self.moveX]
            self.take(mi, mj)
            self.push()
            self._int_pass_turn()
            freedom = self.fill_shape(mi, mj)
            if freedom == 0:
                self._int_rollback(2, changePass=False)
                self._int_pass_turn()
                raise NameError('illegal move: self capturing ' + move)
            self._int_rollback(changePass=False)
            self._int_pass_turn()
            if self.KO_check():
                raise NameError('illegal move: KO found ' + move)
            self.moveX = not self.moveX
        else:
            raise NameError('illegal move ' + move, move)

    def get_position(self, move):
        mi, mj = self.get_coords(move)
        return self._int_board[mi][mj]
