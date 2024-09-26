class GameState:
	def __init__(self, board_state: list, turn_Max: bool, pos_max: list, pos_min: list):

		self.board_state = board_state
		self.turn_Max = turn_Max
		self.pos_max = pos_max
		self.pos_min = pos_min
		self.winner = ""


	def is_terminal(self):
		
		if self.board_state.count(1) == 0:
				self.winner = "Max"
				return True

		elif self.min_pos == self.max_pos:
				self.winner = "Min"
				return True

	def score(self):
		
		if self.board_state.count(1) == 0:
			return 1
		elif self.min_pos == self.max_pos:
			return -1
		else:
			return 0


	def get_possible_moves(self):
		if self.turn_Max:
			moves_max = []
			for i,j in self.max_pos.iteritems():
				moves_max.append(i+1,j)
				moves_max.append(i, j+1)
				moves_max.append(i-1,j)
				moves_max.append(i, j-1)
			for i in moves_max:
				if i != "■":
					moves = [moves_max]

		else:
			moves_min = []
			for i,j in self.min_pos.iteritems():
				moves_min.append(i+1,j)
				moves_min.append(i, j+1)
				moves_min.append(i-1,j)
				moves_min.append(i, j-1)
			for i in moves_min:
				if i != "■":
					moves = [moves_min]
		return moves;
        


	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x, y] = 1 if self.turn_O else -1
		return GameState(new_board_state, not self.turn_O)
		