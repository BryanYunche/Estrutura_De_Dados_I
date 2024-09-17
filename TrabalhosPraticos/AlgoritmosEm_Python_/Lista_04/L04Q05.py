#Implemente um programa em C que lê elementos inteiros e multiplica 
# cada elemento pelo índice do vetor e imprime o vetor resultante.

def main():
    
    n = int(input("Digite a quantidade de elementos: "))
    
    vetor = []

    for i in range(n):
        num = int(input(f"Digite o elemento {i}: "))
        vetor.append(num)
    
    vetor_resultante = [vetor[i] * i for i in range(n)]

    print("Vetor resultante:", vetor_resultante)

 
if __name__ == "__main__":
    main()
