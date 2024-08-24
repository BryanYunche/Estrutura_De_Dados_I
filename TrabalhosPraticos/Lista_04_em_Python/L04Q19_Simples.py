def transposta(m, n, mat):
    return [mat[i * n + j] for j in range(m) for i in range(n)]