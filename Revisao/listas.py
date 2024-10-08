#Listas: É uma estrutura de dados que armazena elementos em uma sequência. 
# Cada elemento tem uma posição específica, e é possível acessar diretamente os elementos pela sua posição.

from lista_escadeada import Lista_encadeada

#Exemplo:
print(20*'=')
lista = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista)

#Encadeadas
exemplo_lista_encadeada = Lista_encadeada()
exemplo_lista_encadeada.adiciona_valor(1)
exemplo_lista_encadeada.adiciona_valor(2)
exemplo_lista_encadeada.adiciona_valor(3)
exemplo_lista_encadeada.adiciona_valor(4)
exemplo_lista_encadeada.adiciona_valor(5)

exemplo_lista_encadeada.imprime_lista()

#Recursivas
#Circulares
