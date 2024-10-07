class state:
    def __init__(self, tabuleiro, pacman:list, ghost:list, turno:bool, Maxdepth:int):
        self.pacman = pacman
        self.ghost = ghost
        self.ghost_last = "1"
        self.turno = turno
        self.tabuleiro = tabuleiro
        self.Maxdepth = Maxdepth
    
    def update(self, move):
        if move is None:
            return self
        if self.turno:
            x,y,z = self.pacman
            self.tabuleiro.get_tabuleiro(z)[x][y] = "0"
            x,y,z = move
            self.tabuleiro.get_tabuleiro(z)[x][y] = "P"
            self.pacman = [x,y,z]
        else:
            oldx, oldy, oldz = self.ghost
            x, y, z = move if move is not None else [-1, -1, -1]
            if x >= 0 and y >= 0 and 3 > z >= 0:  # Verifica se a nova posição é válida
                # Atualiza a posição do fantasma
                if self.tabuleiro.get_tabuleiro(z)[x][y] == "P":
                    # Fantasma captura o Pac-Man
                    self.tabuleiro.get_tabuleiro(z)[x][y] = "P"
                else:
                    self.tabuleiro.get_tabuleiro(oldz)[oldx][oldy] = self.ghost_last
                    self.ghost_last = self.tabuleiro.get_tabuleiro(z)[x][y]
                    # Atualiza para a nova posição do fantasma
                    self.tabuleiro.get_tabuleiro(z)[x][y] = "F"
                # Atualiza a nova posição do fantasma
                self.ghost = [x, y, z]
        return self
    
    def movimentos_validos(self):
        moves = []
        x,y,z = self.pacman if self.turno else self.ghost
        if self.pacman is not None and self.ghost is not None:
            if self.tabuleiro.get_tabuleiro(z)[x-1][y] != "■":
                moves.append([x-1,y,z])
            if self.tabuleiro.get_tabuleiro(z)[x+1][y] != "■":
                moves.append([x+1,y,z])
            if self.tabuleiro.get_tabuleiro(z)[x][y-1] != "■":
                moves.append([x,y-1,z])
            if self.tabuleiro.get_tabuleiro(z)[x][y+1] != "■":
                moves.append([x,y+1,z])
            if z > 0:
                if self.tabuleiro.get_tabuleiro(z-1)[x][y] != "■":
                    moves.append([x,y,z-1])
            if z < 2:
                if self.tabuleiro.get_tabuleiro(z+1)[x][y] != "■":
                    moves.append([x,y,z+1])
        
        return moves
    
    def count_food(self):
        comidas = sum(row.count('1') for layer in self.tabuleiro.get_all() for row in layer)
        return comidas
    
    def isTerminal(self):
        comidas = self.count_food()
        if comidas == 0:
            return True
        elif self.pacman == self.ghost:
            print("Game Over...")
            print("O fantasma Pegou o Pacman")
            return True
        return False
    
    def get_score(self):
        # Se todo a comida foi comida, Pac-Man venceu
        if self.count_food() == 0:
            return float('inf')
        # Se Pac-Man foi capturado pelo fantasma, fantasma venceu
        elif self.pacman == self.ghost:
            return float('-inf')
        else:
            # Calcula a distância entre o fantasma e Pac-Man
            ghost_x, ghost_y, ghost_z = self.ghost
            pacman_x, pacman_y, pacman_z = self.pacman
            
            distance = abs(ghost_x - pacman_x) + abs(ghost_y - pacman_y) + abs(ghost_z - pacman_z)
            return distance  
        
    def get_distance(self):
        ghost_x, ghost_y, ghost_z = self.ghost
        pacman_x, pacman_y, pacman_z = self.pacman
        
        distance = (abs(ghost_x - pacman_x) + abs(ghost_y - pacman_y) + abs(ghost_z - pacman_z))
        return distance  
