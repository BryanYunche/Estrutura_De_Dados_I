#questão_3
numero = input(int('Digite um numero'));

valores = []

print("Digite 20 valores reais:")
for i in range(N):
    valor = float(input(f"Valor {i + 1}: "))
    valores.append(valor)

media = sum(valores) / N

variancia = sum((x - media) ** 2 for x in valores) / N

print(f"A variância dos valores é: {variancia:.2f}")
