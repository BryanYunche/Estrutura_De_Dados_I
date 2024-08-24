def matriz_identidade(mat, n):
    return all(mat[i * n + i] == 1 and all(mat[i * n + j] == 0 for j in range(n) if j != i) for i in range(n))