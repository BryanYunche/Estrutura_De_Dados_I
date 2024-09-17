#Implemente a função deriva, que calcula a derivada de um polinômio. 
# Cada polinômio é definido por um vetor contendo seus coeficientes. 
# Por exemplo, o polinômio de grau 2, 3x2+2x+12, 
# terá um vetor de coeficientes igual a v[ ]={12,2,3}. A função deriva deve obedecer ao protótipo:

def deriva(poli):
    grau = len(poli) - 1
    derivada = [(poli[i] * i) for i in range(1, grau + 1)]
    return derivada

def main():

    grau = int(input("Digite o grau do polinômio: "))

    
    poli = []
    for i in range(grau + 1):
        coef = float(input(f"Digite o coeficiente do termo de grau {i}: "))
        poli.append(coef)

    
    derivada = deriva(poli)

    
    print("Os coeficientes da derivada são:")
    for i, coef in enumerate(derivada):
        print(f"Coeficiente do termo de grau {i}: {coef:.2f}")

if __name__ == "__main__":
    main()
