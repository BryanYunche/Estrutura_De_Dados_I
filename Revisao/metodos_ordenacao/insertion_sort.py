def insertion_sort(lista):
    # Percorre a lista começando do segundo elemento
    for i in range(1, len(lista)):
        # Armazena o valor do elemento atual
        chave = lista[i]
        j = i - 1

        # Move os elementos da lista ordenada para a direita se forem maiores que a chave
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        

        
        # Insere o valor da chave na posição correta
        lista[j + 1] = chave

        print(f'{lista} | Chave: {chave}')

