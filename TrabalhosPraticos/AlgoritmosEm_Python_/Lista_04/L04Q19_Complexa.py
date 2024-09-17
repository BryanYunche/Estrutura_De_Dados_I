#Implemente uma função que calcule a transposta de uma matriz mat. 
# A função tem como valor de retorno o ponteiro do vetor que representa a matriz transposta criada. 
# A implementação dessa função deve ser dada por: float * transposta (int m,int n, float* mat)  OBS:utilizar vetor simples

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
