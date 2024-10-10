#Retorna a lista ordenada pelo método bubble sort e o tempo que levou
import time

def ord_bolha(lista):
    n = len(lista)

    inicio = time.time()
    #I controla o número de interações, as interações serão cada vez menor a cada ciclo
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(f'{lista} -> Iterações feitas: {i}')

    
    print(lista)
    fim = time.time()

    tempo_execucao = fim - inicio
    print(20*'=')
    print(f'Tempo de execução: {tempo_execucao}')
    print(20*'=')