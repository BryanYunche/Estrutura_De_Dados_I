#questão_6 
def media(n: int, v: list[float]) -> float:
    
    return sum(v) / n

def variancia(n: int, v: list[float], m: float) -> float:
    
    return sum((x - m) ** 2 for x in v) / n

def main():
    v = []
    print("Digite 10 números reais:")
    for i in range(10):
        numero = float(input(f"Digite um numero: "))
        v.append(numero)

    n = len(v)
    
    m = media(n, v)
    print(f"Média: {m}")

    var = variancia(n, v, m)
    print(f"Variância: {var}")

if __name__ == "__main__":
    main()
