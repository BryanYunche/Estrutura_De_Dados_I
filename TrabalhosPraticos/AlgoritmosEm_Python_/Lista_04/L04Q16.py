#Implemente a função max_vet, que recebe como parâmetro um vetor de números de 
# ponto flutuante (vet) de tamanho n e retorna o maior número armazenado nesse vetor. 
# Essa função deve obedecer ao protótipo: 

def max_vet(vet):
    if not vet:
        return None  
    
    maior = vet[0]  
    for num in vet[1:]:
        if num > maior:
            maior = num
    return maior