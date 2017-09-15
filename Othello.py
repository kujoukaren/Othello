# Created by KujouKaren on 2017.9.14
# Othello logic module

class Othello:
	def __init__(self, row: int, col: int, turn: str, win: str):
		self._row = row
		self._col = col
		self._turn = turn
		self._win = win
		self._board = self._newBoard(self._row, self._col)
		self.resetBoard()

	def resetBoard(self):
		for row in range(len(self._board)):
			for col in range(len(self._board[0])):
				self._board[row][col] = '.'
		centerX = int(len(self._board))//2
		centerY = int(len(self._board[0]))//2

		self._board[centerX][centerY] = 'B'
		self._board[centerX][centerY-1] = 'W'
		self._board[centerX-1][centerY] = 'W'
		self._board[centerX-1][centerY-1] = 'B'

	def drawBoard(self):
		print('--------------------------------')
		for i in range(len(self._board[0])):
			print(i+1, end=' ')
		print()
		for row in range(len(self._board)):
			for col in range(len(self._board[row])):
				print(self._board[row][col], end=' ')
			print(row+1)

	def countScore(self):
		black = 0
		white = 0
		for row in range(len(self._board)):
			for col in range(len(self._board[row])):
				if self._board[row][col] == 'B':
					black += 1
				elif self._board[row][col] == 'W':
					white += 1
		print('-----Score-----\nBlack:', black, 'White:',white)

	def isMoveValid(self, row: int, col: int) -> bool:
		if not 0 <= row <= self._row and not 0 <= col <= self._col:
			print("ERROR: Position out of range!")
			return False
		if not self._board[row][col] == '.':
			print("ERROR:",self._board[row][col],'is already placed!')
			return False
		up, down, left, right = row-1, row+1, col-1, col+1
		fliped = False
		# check up side
		if up >= 0:
			if not self._board[up][col] == '.' and not self._board[up][col] == self._turn:
				flag = False
				for i in range(row):
					if self._board[row-1-i][col] == self._turn and not flag:
						flag = True
						if flag:
							for j in range(i):
								self._flipDisc(row-1-j, col)
								print(row-1-j,',',col,'fliped')
							fliped = True
		# check down side
		if down < self._row:
			if not self._board[down][col] == '.' and not self._board[down][col] == self._turn:
				flag = False
				for i in range(down, self._row):
					if self._board[i][col] == self._turn and not flag:
						flag = True
						if flag:
							for j in range(down, i):
								self._flipDisc(j, col)
								print(j,',',col,'fliped')
							fliped = True
		# check left side
		if left >= 0:
			if not self._board[row][left] == '.' and not self._board[row][left] == self._turn:
				flag = False
				for i in range(col):
					if self._board[row][col-1-i] == self._turn and not flag:
						flag = True
						if flag:
							for j in range(i):
								self._flipDisc(row, col-1-j)
								print(row,',',col-1-i,'fliped')
							fliped = True
		# check right side
		if right < self._col:
			if not self._board[row][right] == '.' and not self._board[row][left] == self._turn:
				flag = False
				for i in range(right, self._col):
					if self._board[row][i] == self._turn and not flag:
						flag = True
						if flag:
							for j in range(right, i):
								self._flipDisc(row, j)
								print(row,',',j,'fliped')
							fliped = True
		if not fliped:
			print("ERROR: invalid position.")
			return False
		else:
			self._board[row][col] = self._turn
			self._turn_switch()
			return True

	# private
	def _newBoard(self, row: int, col:int):
		board = []
		for i in range(row):
			board.append(['.'] * col)
		return board

	def _flipDisc(self, row: int, col: int):
		if self._board[row][col] == 'B':
			self._board[row][col] = 'W'
		elif self._board[row][col] == 'W':
			self._board[row][col] = 'B'

	def _turn_switch(self):
		print('GAME INFO: Turn switch')
		if self._turn == 'B':
			self._turn = 'W'
		elif self._turn == 'W':
			self._turn ='B'