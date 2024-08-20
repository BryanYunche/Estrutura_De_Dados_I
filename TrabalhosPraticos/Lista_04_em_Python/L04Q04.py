#Implemente um programa em C, que lê dois vetores v e w e calcula o produto dos termos 
# dos vetores armazenando o resultado em y, imprimir o produto entre os termos dos 
# vetores (valores armazenados em y).

def CalulosEntreVetores(vetor01, vetor02):
    if len(vetor01) == len(vetor02):
       iteracaoMaxima = len(vetor01)
    elif len(vetor01) > len(vetor02):
       iteracaoMaxima = len(vetor02)
    else:
       iteracaoMaxima = len(vetor01)
       

    