#8)Implemente uma função em C que calcula o produto vetorial de dois vetores 
# usar alocação dinâmica a função produto vetorial é mostrada a seguir: 

def produtoVetorial(vetor01, vetor02):
    # Calcula o produto vetorial
    produto = [
        vetor01[1] * vetor02[2] - vetor02[1] * vetor01[2],
        vetor01[2] * vetor02[0] - vetor02[2] * vetor01[0],
        vetor01[0] * vetor02[1] - vetor02[0] * vetor01[1]
    ]
    return produto

# Exemplo de uso:
u = [54, 2, 65]
v = [98, 1, 75]

print("Produto vetorial: ", produtoVetorial(u, v))
