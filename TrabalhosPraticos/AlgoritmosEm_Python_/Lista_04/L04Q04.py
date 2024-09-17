#Implemente um programa em C, que lê dois vetores v e w e calcula o produto dos termos 
# dos vetores armazenando o resultado em y, imprimir o produto entre os termos dos 
# vetores (valores armazenados em y).

def CalculosEntreVetores(vetor01, vetor02):
   if len(vetor01) == len(vetor02):
      iteracaoMaxima = len(vetor01)
   elif len(vetor01) > len(vetor02):
      iteracaoMaxima = len(vetor02)
   elif len(vetor01) < len(vetor02):
      iteracaoMaxima = len(vetor01)

   listaProduto = []
   for i in range(iteracaoMaxima):
     listaProduto.append(vetor01[i]*vetor02[i])

   return listaProduto

listaTeste01 = [434, 432, 44, 54, 67, 654, 35, 98]
listaTeste02 = [78, 93, 234, 4, 6, 232, 948]

print(CalculosEntreVetores(listaTeste01, listaTeste02))
   
        