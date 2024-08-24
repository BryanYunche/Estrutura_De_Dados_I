#questao  11
def print_diagonal_and_sum(matrix):
    diagonal_elements = []
    diagonal_sum = 0
    
    for i in range(len(matrix)):
        diagonal_elements.append(matrix[i][i])
        diagonal_sum += matrix[i][i]
    
    print("Elementos da diagonal principal:", diagonal_elements)
    print("Soma dos elementos da diagonal principal:", diagonal_sum)

def main():

    matrix = []
    print("Digite os valores da matriz 3x3:")
    
    for i in range(3):
        row = []
        for j in range(3):
            value = float(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
            row.append(value)
        matrix.append(row)
    
    print("\nMatriz inserida:")
    for row in matrix:
        print(row)
    
    print_diagonal_and_sum(matrix)

if __name__ == "__main__":
    main()
