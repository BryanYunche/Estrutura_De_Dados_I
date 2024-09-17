#Implemente um programa em C que calcula a média de um conjunto de 20 valores lidos
#de um vetor, sendo esses valores reais. 

vetor = [i for i in range(7, 27)]

print(f'Tamanho do vetor: {len(vetor)}')
print(f'Conteúdo do vetor: {vetor}')
print(f'Média do vetor: {sum(vetor)/len(vetor)}')

