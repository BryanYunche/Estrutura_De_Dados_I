def insertion_sort(arr):
    """Função auxiliar para ordenar um balde usando Insertion Sort."""
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def bucket_sort(lista):
    if len(lista) == 0:
        return lista

    # Encontrar o valor mínimo e máximo
    valor_min = min(lista)
    valor_max = max(lista)

    # O número de baldes é escolhido arbitrariamente ou com base no tamanho da lista
    numero_de_baldes = len(lista)

    # Inicializar os baldes como listas vazias
    baldes = [[] for _ in range(numero_de_baldes)]

    # Determinar o intervalo de cada balde
    intervalo = (valor_max - valor_min + 1) // numero_de_baldes + 1

    # Coloca os elementos da lista nos baldes adequados
    for numero in lista:
        # Encontra o índice do balde para o número
        indice_do_balde = (numero - valor_min) // intervalo
        baldes[indice_do_balde].append(numero)

    # Ordenar cada balde individualmente usando insertion sort
    for balde in baldes:
        insertion_sort(balde)

    # Concatenar todos os baldes para formar a lista final ordenada
    lista_ordenada = []
    for balde in baldes:
        lista_ordenada.extend(balde)

    print(f'Lista ordenada: {lista_ordenada}')