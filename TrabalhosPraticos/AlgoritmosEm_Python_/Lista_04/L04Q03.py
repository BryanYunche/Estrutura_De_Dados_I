#Implemente um programa em C que calcula  a variância de um conjunto de 20 valores lidos, 
# sendo esses valores reais


N = 20

# Lista para armazenar os valores
valores = []

print("Digite 20 valores reais:")

# Lendo 20 valores reais
for i in range(N):
    valor = float(input(f"Valor {i + 1}: "))
    valores.append(valor)

# Calculando a média dos valores
media = sum(valores) / N

# Calculando a variância
variancia = sum((x - media) ** 2 for x in valores) / N

# Exibindo a variância
print(f"A variância dos valores é: {variancia:.2f}")