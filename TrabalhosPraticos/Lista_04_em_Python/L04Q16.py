def max_vet(vet):
    if not vet:
        return None  
    
    maior = vet[0]  
    for num in vet[1:]:
        if num > maior:
            maior = num
    return maior