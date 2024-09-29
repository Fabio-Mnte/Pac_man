class GameState:
	def __init__(self, board_state: list, turn_Max: bool, pos_max: list, pos_min: list):

		self.board_state = board_state
		self.turn_Max = turn_Max
		self.pos_max = pos_max
		self.pos_min = pos_min
		self.winner = ""


	def is_terminal(self):

		if self.board_state[0].count('1') == 0 and self.board_state[1].count('1') == 0 and self.board_state[2].count('1') == 0:
				self.winner = "Max"
				return True	
		elif self.pos_min == self.pos_max:
				self.winner = "Min"
				return True
		
		print(self.board_state[0].count('1'))
		print(self.board_state[1].count('1'))
		print(self.board_state[2].count('1'))
		return False

	def score(self, state: list, old_pos:list, move:list):
		new_board_state = self.board_state.copy()
		x, y, z = old_pos[0], old_pos[1], old_pos[2]
		new_board_state[z][x, y] = "0" if self.turn_Max else "1"
		x, y, z = move[0], move[1], move[2] 
		new_board_state[z][x, y] = "P" if self.turn_Max else "F"
		if new_board_state[0].count('1') == 0 and new_board_state[1].count('1') and new_board_state[2].count('1'):
			return 1
		elif self.pos_min == self.pos_max:
			return -1
		else:
			return 0


	def get_possible_moves(self):

		if self.turn_Max:
			moves_max = []
			for i,j,l in self.pos_max:
				if self.board_state[l].get(i+1,j) != "■":
					moves_max.append(i+1,j, l)
				if self.board_state[l].get(i,j+1) != "■":
					moves_max.append(i, j+1, l)
				if self.board_state[l].get(i-1,j) != "■":
					moves_max.append(i-1,j, l)
				if self.board_state[l].get(i,j-1) != "■":
					moves_max.append(i, j-1, l)
				if l<3:
					if self.board_state[l+1].get(i,j) != "■":
						moves_max.append(i,j,l+1)
				if l>0 :
					if self.board_state[l-1].get(i,j) != "■":
						moves_max.append(i,j,l-1)
			moves = [moves_max]
		else:
			moves_min = []
			for i,j,l in self.pos_min:
				if self.board_state[l].get(i+1,j,l) != "■":
					moves_min.append(i+1,j,l)
				if self.board_state[l].get(i,j+1,l) != "■":
					moves_min.append(i,j+1,l)
				if self.board_state[l].get(i-1,j,l) != "■":
					moves_min.append(i-1,j,l)
				if self.board_state[l].get(i,j-1,l) != "■":
					moves_min.append(i,j-1,l)
				if l<3:
					if self.board_state[l+1].get(i,j) != "■":
						moves_min.append(i,j,l+1)
				if l>0:
					if self.board_state[l-1].get(i,j) != "■":
						moves_min.append(i,j,l-1)
			moves = [moves_min]
		return moves;

	def get_new_state(self, old_pos, move):
		new_board_state = self.board_state.copy()
		x, y, z = old_pos[0], old_pos[1], old_pos[2]
		new_board_state[z][x, y] = "0" if self.turn_Max else "1"
		x, y, z = move[0], move[1], move[2] 
		new_board_state[z][x, y] = "P" if self.turn_Max else "F"
		return GameState(new_board_state, not self.turn_Max)
		