#Implemente a função pares, que recebe como parâmetros um vetor de números inteiros 
# (vet) de tamanho n e retorna quantos números pares estão armazenados nesse vetor. 
# Essa função deve obedecer ao protótipo.

def pares(vet):
    count = 0
    for num in vet:
        if num % 2 == 0:
            count += 1
    return count

n = int(input("Digite o tamanho do vetor: "))

vetor = []
for i in range(n):
    elemento = int(input(f"Digite o elemento {i + 1} do vetor: "))
    vetor.append(elemento)

resultado = pares(vetor)
print(f"Número de elementos pares no vetor: {resultado}")
