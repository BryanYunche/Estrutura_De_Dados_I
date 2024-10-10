#Teste de ordenação para vários tipos de ordenação

lista_desordenada = [34, 12, 45, 23, 9, 67, 81]

print(20*'=+=')
print(lista_desordenada)
print(20*'=+=')
#Testa o Bubble Sort ------------------------------------------------
from bubble_sort import ord_bolha

ord_bolha(lista_desordenada)

#Teste de ordenação do Insertion Sort -------------------------------
from insertion_sort import insertion_sort
lista_desordenada = [34, 12, 45, 23, 9, 67, 81]

print(20*'=+=')
print(lista_desordenada)
print(20*'=+=')

insertion_sort(lista_desordenada)

#Teste de ordenação por couting sort --------------------------------
from coutingSort import count_sort
lista_desordenada = [34, 12, 45, 23, 9, 34, 67, 23, 98, 67, 81]

print(20*'=+=')
print(lista_desordenada)
print(20*'=+=')

count_sort(lista_desordenada)

#Teste de ordenação por bucket sort --------------------------------
from bucketSort import bucket_sort
lista_desordenada = [34, 12, 45, 23, 9, 34, 67, 23, 98, 67, 81]

print(20*'=+=')
print(lista_desordenada)
print(20*'=+=')

bucket_sort(lista_desordenada)