
#queestao_19
def transposta(m, n, mat):
    
    transposta = [0.0] * (m * n)
    
    for i in range(m):
        for j in range(n):
            
            transposta[j * m + i] = mat[i * n + j]
    
    return transposta


m = int(input("Digite o número de linhas da matriz: "))
n = int(input("Digite o número de colunas da matriz: "))


mat = []
print("Digite os valores da matriz:")
for i in range(m):
    for j in range(n):
        valor = float(input(f"Digite o valor para a posição ({i + 1},{j + 1}): "))
        mat.append(valor)


mat_transposta = transposta(m, n, mat)


print("\nMatriz Transposta:")
for i in range(n):
    for j in range(m):
        print(f"{mat_transposta[i * m + j]:.2f}", end=" ")
    print()
