#questao_17
def busca(n, vet, x):
    for i in range(n):
        if vet[i] == x:
            return i  
    return 0  

n = int(input("Digite o tamanho do vetor: "))
vet = []

for i in range(n):
    num = float(input(f"Digite o valor {i + 1}: "))
    vet.append(num)

x = float(input("Digite o valor que deseja buscar no vetor: "))

resultado = busca(n, vet, x)

if resultado != 0:
    print(f"O valor {x} foi encontrado na posição {resultado}.")
else:
    print(f"O valor {x} não foi encontrado no vetor.")
