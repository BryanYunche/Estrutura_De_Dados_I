#Implemente a função negativos, que recebe como parâmetro um vetor de números de  
# ponto flutuante (vet) de tamanho n e retorna quantos números negativos estão 
# armazenados nesse vetor. Essa função deve obedecer ao protótipo:

def conta_negativos(vetorN):
    cont = 0
    for i in vetorN:
        if i < 0:
            cont += 1
    return cont

vetorTeste = [1.4, 4.2, 4.27, 867.3, -2.1, 9.1, -5.8, -3.9, -2.7, 0, -9.3, 7.4]

print(conta_negativos(vetorTeste))