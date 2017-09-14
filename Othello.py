# Mengqi Li 92059150
# Othello logic module


class Othello:
    def __init__(self, row: int, col: int, turn: str, win: str):
        self._row = row
        self._col = col
        self._turn = turn
        self._win = win
        self._board = self._newBoard(self._row, self._col)
        self.resetBoard()

    # public
    def get_board(self) -> list:
        return self._board
    
    def resetBoard(self):
        for i in range(len(self._board)):
            for j in range(len(self._board[0])):
                self._board[i][j] = '.'
        centerX = int(len(self._board))//2
        centerY = int(len(self._board[0]))//2
        self._board[centerX][centerY] = 'B'
        self._board[centerX][centerY-1] = 'W'
        self._board[centerX-1][centerY] = 'W'
        self._board[centerX-1][centerY-1] = 'B'
        
    def drawBoard(self):
        print('-------------------------')
        for i in range(len(self._board[0])):
            print(i+1, end=' ')
        print()
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                print(self._board[i][j], end=' ')
            print(i+1)

    def countScore(self):
        black = 0
        white = 0
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == 'B':
                    black += 1
                elif self._board[i][j] == 'W':
                    white += 1
        print('----Score----\nBlack:', black, ' White:', white)

    def isValidMove(self, row: int, col: int) -> bool:
        
        if not 0 <= row <= self._row and\
           not 0 <= col <= self._col:
            return False
        if not self._board[row][col] == '.':
            print(self._board[row][col],'is placed')
            return False

        up, right, down, left = row-1, col+1, row+1, col-1
        fliped = False
        if up >= 0:
            if not self._board[up][col] == self._turn and\
               not self._board[up][col] == '.':
                flag = False
                for i in range(up+1):
                    if self._board[i][col] == self._turn and\
                       not flag:
                        flag = True
                        if flag:
                            for j in range(i+1, up+1):
                                self._flipDisc(j, col)
                                print('fliped')
                            fliped = True
        if right < self._col-right:
            if not self._board[row][right] == self._turn and\
               not self._board[row][right] == '.':
                flag = False
                for i in range(right, self._col):
                    if self._board[row][i] == self._turn and\
                       not flag:
                        flag = True
                        if flag:
                            for j in range(right, i):
                                self._flipDisc(row, j)
                                print('fliped')
                            fliped = True
        if down < self._row:
            if not self._board[down][col] == self._turn and\
               not self._board[down][col] == '.':
                flag = False
                for i in range(down, self._row):
                    if self._board[i][col] == self._turn and\
                       not flag:
                        flag = True
                        if flag:
                            for j in range(down, i):
                                self._flipDisc(j, col)
                                print('fliped')
                            fliped = True
        if left >= 0:
            if not self._board[row][left] == self._turn and\
               not self._board[row][left] == '.':
                flag = False
                for i in range(left+1):
                    if self._board[row][i] == self._turn and\
                       not flag:
                        flag = True
                        if flag:
                            for j in range(i+1, left+1):
                                self._flipDisc(row, j)
                                print('fliped')
        print(fliped)
        if not fliped:
            return False
        
        self._board[row][col] = self._turn
        self._turn_switch()
        return True
            
                

    # private
    def _newBoard(self, row: int, col: int):
        board = []
        for i in range(row):
            board.append(['.'] * col)
        return board

    def _turn_switch(self):
        print('turn switch')
        if self._turn == 'B':
            self._turn = 'W'
        elif self._turn == 'W':
            self._turn = 'B'

    def _flipDisc(self, row: int, col: int):
        if self._board[row][col] == 'B':
            self._board[row][col] = 'W'
        elif self._board[row][col] == 'W':
            self._board[row][col] = 'B'
        



















        
