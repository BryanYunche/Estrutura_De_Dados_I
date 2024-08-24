#questao_15
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
