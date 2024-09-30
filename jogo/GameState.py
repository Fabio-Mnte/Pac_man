class GameState:
	def __init__(self, board_state: list, turn_Max: bool, pos_max: list, pos_min: list):
		self.board_state = board_state
		self.turn_Max = turn_Max
		self.pos_max = pos_max
		self.pos_min = pos_min
		self.winner = ""


	def is_terminal(self):
		comidas = 0
		for i in self.board_state[0], self.board_state[1], self.board_state[2]:
			comidas += i.count('1')
		for i in self.board_state[1]:
			comidas += i.count('1')
		for i in self.board_state[2]:
			comidas += i.count('1')
		if comidas == 0:
				self.winner = "Max"
				return True, self.winner	
		elif self.pos_min == self.pos_max:
				self.winner = "Min"
				return True, self.winner	
		#print(comidas)
		return False
	
	def get_depth(self):
		comidas = 0
		for i in self.board_state[0]:
			comidas += i.count('1')
		for i in self.board_state[1]:
			comidas += i.count('1')
		for i in self.board_state[2]:
			comidas += i.count('1')
		return comidas

	def score(self, old_pos:list, move:list):
		comidas = 0
		try:
			new_board_state = self.board_state.copy()
			x, y, z = old_pos[0], old_pos[1], old_pos[2]
			new_board_state[z][x][y] = "0" if self.turn_Max else "1"
			x, y, z = move[0], move[1], move[2] 
			new_board_state[z][x][y] = "P" if self.turn_Max else "F"
			for i in self.board_state[0]:
				comidas += i.count('1')
			for i in self.board_state[1]:
				comidas += i.count('1')
			for i in self.board_state[2]:
				comidas += i.count('1')
			if comidas == 0:
				return 1
			elif self.pos_min == self.pos_max:
				return -1
			else:
				return 0
		except:
			for i in self.board_state[0]:
				comidas += i.count('1')
			for i in self.board_state[1]:
				comidas += i.count('1')
			for i in self.board_state[2]:
				comidas += i.count('1')
			if comidas == 0:
				return 1
			elif self.pos_min == self.pos_max:
				return -1
			else:
				return 0
	
	def get_possible_moves(self):
		if self.turn_Max:
			moves_max = []
			i, j, l = self.pos_max
			if self.board_state[l][i+1][j] != "■":
				moves_max.append([i+1,j, l])
			if self.board_state[l][i][j+1] != "■":
				moves_max.append([i,j+1,l])
			if self.board_state[l][i-1][j] != "■":
				moves_max.append([i-1,j, l])
			if self.board_state[l][i][j-1] != "■":
				moves_max.append([i, j-1, l])
			if l<3:
				if self.board_state[l+1][i][j] != "■":
					moves_max.append([i,j,l+1])
			if l>0 :
				if self.board_state[l-1][i][j] != "■":
					moves_max.append([i,j,l-1])
			moves = moves_max
		if not self.turn_Max:
			moves_min = []
			i, j, l = self.pos_max
			if self.board_state[l][i+1][j] != "■":
				moves_min.append([i+1,j, l])
			if self.board_state[l][i][j+1] != "■":
				moves_min.append([i,j+1,l])
			if self.board_state[l][i-1][j] != "■":
				moves_min.append([i-1,j, l])
			if self.board_state[l][i][j-1] != "■":
				moves_min.append([i, j-1, l])
			if l<3:
				if self.board_state[l+1][i][j] != "■":
					moves_min.append([i,j,l+1])
			if l>0 :
				if self.board_state[l-1][i][j] != "■":
					moves_min.append([i,j,l-1])
			moves = moves_min
		return moves
	
	def straight_distance(self):
		return abs((self.pos_max[0] - self.pos_min[0]) + (self.pos_max[1] - self.pos_max[1]))
	
	def heuristica_manhattan(pacman_pos, ghost_pos):
		return abs(pacman_pos[0] - ghost_pos[0]) + abs(pacman_pos[1] - ghost_pos[1])
	
	def is_valid_position(self, x, y):
		board = self.board_state
		rows = len(board)
		columns = len(board[0])
			
		return 0 <= x < rows and 0 <= y < columns and board[x][y] != '■'
	
	def posicao_valida(board, x, y):
		linhas = len(board)
		colunas = len(board[0])
		return 0 <= x < colunas and 0 <= y < linhas and board[x][y] != "■"

	def get_new_state(self, old_pos, move):
		new_board_state = self.board_state.copy()

		x, y, z = old_pos[0], old_pos[1], old_pos[2]
		new_board_state[z][x][y] = "0" if self.turn_Max else "1"

		x, y, z = move[0], move[1], move[2]
		new_board_state[z][x][y] = "P" if self.turn_Max else "F"

		if self.turn_Max:
			self.pos_max = [x, y, z]
		else:
			self.pos_min = [x, y, z]
		
		return GameState(new_board_state, not self.turn_Max, self.pos_max, self.pos_min)



		