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
		for i in self.board_state[0], self.board_state[1], self.board_state[2]:
			comidas += i.count('1')
		for i in self.board_state[1]:
			comidas += i.count('1')
		for i in self.board_state[2]:
			comidas += i.count('1')
		return comidas


	def score(self, old_pos:list, move:list):
		try:
			new_board_state = self.board_state.copy()
			x, y, z = old_pos[0], old_pos[1], old_pos[2]
			new_board_state[z][x][y] = "0" if self.turn_Max else "1"
			x, y, z = move[0], move[1], move[2] 
			new_board_state[z][x][y] = "P" if self.turn_Max else "F"
			if new_board_state[0].count('1') == 0 and new_board_state[1].count('1') and new_board_state[2].count('1'):
				return 1
			elif self.pos_min == self.pos_max:
				return -1
			else:
				return 0
		except:
			if new_board_state[0].count('1') == 0 and new_board_state[1].count('1') and new_board_state[2].count('1'):
				return 1
			elif self.pos_min == self.pos_max:
				return -1
			else:
				return 0
	
	def get_possible_moves(self):
		if not self.turn_Max:
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
		return moves;

	def get_new_state(self, old_pos, move):
		new_board_state = self.board_state.copy()
		x, y, z = old_pos[0], old_pos[1], old_pos[2]
		new_board_state[z][x][y] = "0" if self.turn_Max else "1"
		if move[0] != -1 and move[1] != -1 and move[2] != -1:
			x, y, z = move[0], move[1], move[2]
			new_board_state[z][x][y] = "P" if self.turn_Max else "F"
			if self.turn_Max:
				self.pos_max = [x, y, z]
			else:
				self.pos_min = [x, y, z]
		
		return GameState(new_board_state, not self.turn_Max, self.pos_max if self.turn_Max else self.pos_min, self.pos_min if self.turn_Max else self.pos_max)

		