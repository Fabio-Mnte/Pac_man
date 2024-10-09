# Função Minimax

```python
def MinMax(state, moves, depth, turno):
    if turno:  # Se for turno do Max (Jogador Humano) - O(1)
        best_score = float('-inf')
        best_move = None
    else:  # Se for turno do Min (Fantasma)
        best_score = float('inf')
        best_move = None

    if depth == 0 or state.isTerminal(): #O(1)
        score = state.get_score() # O(1)
        return [None, score]

    # Itera pelos movimentos possíveis
    for move in moves: # O(n)
        next_state = state.update(move) # O(1)
        _, current_score = MinMax(next_state, next_state.movimentos_validos(), depth - 1, not turno) # O(n^(d-1))
        if turno:  # Maximiza para o Jogador Humano #O(1)
            if current_score > best_score: #O(1)
                best_score = current_score
                best_move = move
        else:  # Minimiza para o Fantasma
            if current_score < best_score: # O(1)
                best_score = current_score
                best_move = move
    return [best_move, best_score]

```
# Calculo de Complexidade de Tempo
n-->numero de estados
d-->profundidade
v--> vertices vizinhos
T = O(n)*O(n)*O(n^(d-v))  
T = O(n²)*O(n^(d-v))  
T = O(n^(d-v))  

Função Polinomial:  
O(n^(d-v)) → quando encontra o caminho  
O(n^d) → quando não encontra o caminho  
Função Assintótica:  
O(n^(d-v)) → quando encontra o caminho  
O(n^d) → quando não encontra o caminho  


# Função Hill Climbing

```python
def HillClimb(gamestate: state, depth, moves = []):
    if depth == 0:# O(1)
        return [None, gamestate.get_distance()]
    moves = gamestate.movimentos_validos() #O(1)
    melhor_distancia = gamestate.get_distance() #O(1)
    melhorou = True# O(1)
    melhor_movimento = moves[0]# O(1)


    while melhorou: #O(n)
        melhorou = False


        for move in moves: #O(m*n)
            next_state = state.update(gamestate, move) #O(1)
           
            _, distancia_nova = HillClimb(next_state, depth - 1r) #O(n^(d-1))

            if distancia_nova < melhor_distancia or distancia_nova == 0: #O(1)
                melhor_distancia = distancia_nova# O(1)
                melhor_movimento = move# O(1)
                melhorou = True# O(1)

    return melhor_movimento, melhor_distancia# O(1)

```

# Calculo de Complexidade de Tempo

m--> movimentos
n--> numero de estados
d--> profundidade
T = O(n)*O(m*n)*O(n^(d-1))  
O(n²*m)* O(n^(d-1))  
O(n^(2 + d -1)*m) 
O(n^(d+1)*m)  
O((n^d)*m)  
Função Polinomial:  
O((n^d)*m)  
Função Assintótica:  
O((n^d)*m)  
