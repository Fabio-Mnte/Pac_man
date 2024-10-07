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
        next_state = state.update(move) # O(n)
        _, current_score = MinMax(next_state, next_state.movimentos_validos(), depth - 1, not turno) # O(n^(d-1))
        if turno:  # Maximiza para o Jogador Humano #O(1)
            if current_score > best_score:
                best_score = current_score
                best_move = move
        else:  # Minimiza para o Fantasma
            if current_score < best_score: # O(1)
                best_score = current_score
                best_move = move
    return [best_move, best_score]

```
# Calculo de Complexidade de Tempo

T = O(n) * O(n) * O(n^(d-1))
T = (n*n)*n^(d-1)
T= n^2*n^(d-1)
T = O(n^d) --> Complexidade de tempo exponencial

# Função Hill Climbing

```python
def HillClimb(gamestate: state, depth, moves = []):
    if depth == 0: #O(1)
        return [None, gamestate.get_distance()]
    moves = gamestate.movimentos_validos() #O(1)
    melhor_distancia = gamestate.get_distance()#O(1)
    melhorou = True
    melhor_movimento = moves[0]

    while melhorou: # O(1)
        melhorou = False #O(1)
        
        for move in moves: #O(n)
            next_state = state.update(gamestate, move) # O(n)
        
            distancia_nova = next_state.get_distance() #O(1)

            if distancia_nova < melhor_distancia: #O(1)
                melhor_distancia = distancia_nova
                melhor_movimento = move
                melhorou = True

        


    return melhor_movimento, melhor_distancia

```

# Calculo de Complexidade de Tempo

O(1) + O(n)*O(n) + O(1)
O(n*n) + O(1)
O(n^2) --> O tempo de complexidade desse algoritmo seria O(n^2), devido a contagem de n^2 interações