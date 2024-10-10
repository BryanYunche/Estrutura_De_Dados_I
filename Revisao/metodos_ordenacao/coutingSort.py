def count_sort(lista):
    # Encontra o valor máximo da lista
    val_max = max(lista) + 1
    
    # Inicializa as listas auxiliares
    lista_indices = [0] * val_max  # Para contar a ocorrência de cada número
    lista_cont = [0] * val_max  # Para armazenar as posições acumuladas
    lista_ordenada = [0] * len(lista)  # Para armazenar a lista final ordenada

    # Passo 1: Conta as ocorrências de cada número
    for numero in lista:
        lista_indices[numero] += 1

    # Passo 2: Calcula as posições acumuladas
    lista_cont[0] = lista_indices[0]
    for i in range(1, val_max):
        lista_cont[i] = lista_cont[i - 1] + lista_indices[i]

    # Passo 3: Coloca os números nas posições corretas na lista ordenada
    for numero in reversed(lista):  # Reverso para garantir estabilidade
        lista_ordenada[lista_cont[numero] - 1] = numero
        lista_cont[numero] -= 1

    # Imprime a lista ordenada
    print("Lista ordenada:", lista_ordenada)

# Exemplo de uso
lista = [4, 2, 2, 8, 3, 3, 1]
count_sort(lista)

