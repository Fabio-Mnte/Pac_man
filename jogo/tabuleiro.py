class tabuleiro:
    def __init__(self):
        self.andar1 = self.andar1()
        self.andar2 = self.andar2()
        self.andar3 = self.andar3()

    def criar_tabuleiro(self): 
        tabuleiro = [["■" if i == 0 or j == 0 or i == 10 or j == 10 else "1" for j in range(11)] for i in range(11)]
        return tabuleiro
    
    def get_tabuleiro(self, num):
        if num == 0 : return self.andar1
        if num == 1 : return self.andar2
        if num == 2 : return self.andar3
    
    def get_all(self):
        return [self.andar1, self.andar2, self.andar3]

    def imprimir_tabuleiro(self, num):
        for linha in self.get_tabuleiro(num):
            print(' '.join(str(celula) for celula in linha))

    def andar1(self):
        tabuleiro1 = self.criar_tabuleiro()
        paredes = [[2, 1], [2, 3], [2, 5], [2, 6], [2, 7], [2, 9],
                  [3, 3], [4, 2], [4, 3], [4, 5], [4, 7], [4, 8],
                  [5, 5], [5, 7], [6, 4], [6, 5], [6, 7], [6, 9],
                  [7, 7], [8, 2], [8, 3], [8, 5], [8, 6], [8, 7], [8, 9]]
        for parede in paredes:
            i, j = parede
            tabuleiro1[i][j] = "■"
            tabuleiro1[1][1] = "P"
            tabuleiro1[9][9] = "F"
        return tabuleiro1
    
    def andar2(self):
        tabuleiro2 = self.criar_tabuleiro()
        paredes = [[1, 6], [2, 2], [2, 4], [2, 6], [2, 8],
                  [3, 2], [3, 4], [3, 8], [4, 4], [4, 5], [4, 7], [4, 8],
                  [5, 2], [5, 8], [6, 2], [6, 6], [6, 8],
                  [7, 4], [7, 6], [8, 1], [8, 2], [8, 4], [8, 6], [8, 9],
                  [9, 4]]

        for parede in paredes:
            i, j = parede
            tabuleiro2[i][j] = "■"
        return tabuleiro2
    
    def andar3(self):
        tabuleiro3 = self.criar_tabuleiro()
        paredes = [[1, 6], [2, 2], [2, 5], [2, 6], [2, 7], [2, 8],
                  [3, 2], [4, 2], [4, 4], [4, 5], [4, 6], [4, 8],
                  [5, 6], [5, 8], [6, 2], [6, 4], [6, 5], [6, 6],
                  [7, 2], [8, 2], [8, 3], [8, 6], [8, 7], [8, 8], [9, 3]]
        for parede in paredes:
            i, j = parede
            tabuleiro3[i][j] = "■"
        return tabuleiro3


